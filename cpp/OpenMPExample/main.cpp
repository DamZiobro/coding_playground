# include <iostream>
# include <cstdlib>
# include <iostream>
# include <iomanip>
# include <omp.h>
# include <string.h>
# include <stdio.h>

#define THREADS_NUMBER 100

using namespace std;

int main()
{

	int NumOfElements = 100000;

	//=====================================================================

	double average=0.0, A[NumOfElements];
	int i;

	//fullfiling A array
	for(int i=0;i<NumOfElements;i++){
		if(i%2==0){
			A[i] = 1;
		} else {
			A[i] = 3;
		}
	}

	omp_set_dynamic( 0 );
	omp_set_num_threads( omp_get_num_procs());

	double ompTime = omp_get_wtime ();

	double pi, sum = 0.0;
	double step = 1.0/(double) NumOfElements;

	omp_set_num_threads(4);
	#pragma omp parallel for reduction(+:sum)
	for (i=0;i< NumOfElements; i++){
		double x = (i+0.5)*step;
		sum = sum + 4.0/(1.0+x*x);
	}
	pi = step * sum;
	cout << "Pi OMP: " << pi << endl;

	ompTime = omp_get_wtime ( ) - ompTime;


	//=====================================================================

	double normalWorkTime = omp_get_wtime ();

	sum = 0.0;
	step = 1.0/(double) NumOfElements;
	for (i=0;i< NumOfElements; i++){
		double x = (i+0.5)*step;
		sum = sum + 4.0/(1.0+x*x);
	}
	pi = step * sum;
	cout << "Pi Normal: " << pi << endl;

	normalWorkTime = omp_get_wtime ( ) - normalWorkTime;

	//=====================================================================

	std::cout << "ompTime:        " << ompTime << std::endl;
	std::cout << "normalWorkTime: " << normalWorkTime << std::endl;

	return 0;
}


/*int main ( int argc, char *argv[] ){
  double wtime;

  wtime = omp_get_wtime ( );

  char const* str = "Hello world";

  #pragma omp parallel for
  for (unsigned thread = 0; thread < 100000; ++thread){
	  std::cout << str << std::endl;
  }

  wtime = omp_get_wtime ( ) - wtime;
  std::cout << "timeOfWork: " << wtime << std::endl;

  cout << "  Number of processors available = " << omp_get_num_procs ( ) << "\n";
  cout << "  Max number of threads = " << omp_get_max_threads ( ) << "\n";

  return 0;
}
*/
