/*************************************************************************************//**
 *  @file       main.c
 *
 *  @brief      Main entry to C-based application  
 *
 *  @author     Damian Ziobro - XMementoIT Limited (damian@xmementoit.com)
 *         
 **************************************************************************************/


#include <gst/gst.h>
#include <glib.h>


static gboolean
bus_call (GstBus     *bus,
          GstMessage *msg,
          gpointer    data)
{
  GMainLoop *loop = (GMainLoop *) data;

  switch (GST_MESSAGE_TYPE (msg)) {

    case GST_MESSAGE_EOS:
      g_print ("End of stream\n");
      g_main_loop_quit (loop);
      break;

    case GST_MESSAGE_ERROR: 
    {
      gchar  *debug;
      GError *error;

      gst_message_parse_error (msg, &error, &debug);
      g_free (debug);

      g_printerr ("Error: %s\n", error->message);
      g_error_free (error);

      g_main_loop_quit (loop);
      break;
    }

    default:
      break;
  }

  return TRUE;
}


/******** Function ************************************************//**
 *   @brief     main entry Function
 *
 *   @param     argc - number of parameters pass to the application from 
 *                 command line input (stdin)
 *   @param     argv - array of parameters pass to the application from 
 *                 command line input (stdin)
 *
 *   @return    exit code of the application
 *********************************************************************/

int
main (int   argc,
      char *argv[])
{
  GMainLoop *loop;

  GstElement *src, *sink, *pipeline;
  GstBus *bus;
  guint bus_watch_id;

  /* Initialisation */
  gst_init (&argc, &argv);

  loop = g_main_loop_new (NULL, FALSE);

  /* Create gstreamer elements */
  pipeline = gst_pipeline_new ("dvbbasebintest");
  src   = gst_element_factory_make ("dvbbasebin",       "dvbbasebin");
  sink  = gst_element_factory_make ("filesink",      "filesink");

  if (!pipeline || !src || !sink ) {
    g_printerr ("One element could not be created. Exiting.\n");
    return -1;
  }

  /* Set up the pipeline */

  /* we set the input filename to the source element */
  g_object_set (G_OBJECT (src), "modulation", 3, NULL); //QAM-64
  g_object_set (G_OBJECT (src), "trans-mode", 1, NULL); //8k
  g_object_set (G_OBJECT (src), "bandwidth", 0, NULL); //8MHz
  g_object_set (G_OBJECT (src), "frequency", 682000000, NULL);
  g_object_set (G_OBJECT (src), "code-rate-lp", 9, NULL); //auto
  g_object_set (G_OBJECT (src), "code-rate-hp", 2, NULL); //2/3
  g_object_set (G_OBJECT (src), "guard", 3, NULL); //4
  g_object_set (G_OBJECT (src), "hierarchy", 0, NULL); //0
  g_object_set (G_OBJECT (src), "program-numbers", "4170", NULL); //0

  g_object_set (G_OBJECT (sink), "location", "/tmp/out.ts", NULL);

  /* we add a message handler */
  bus = gst_pipeline_get_bus (GST_PIPELINE (pipeline));
  bus_watch_id = gst_bus_add_watch (bus, bus_call, loop);
  gst_object_unref (bus);

  /* we add all elements into the pipeline */
  /* file-source | ogg-demuxer | vorbis-decoder | converter | alsa-output */
  gst_bin_add_many (GST_BIN (pipeline), src, sink, NULL);

  /* we link the elements together */
  /* file-source -> ogg-demuxer ~> vorbis-decoder -> converter -> alsa-output */
  gst_element_link (src, sink);


  /* Set the pipeline to "playing" state*/
  g_print ("Now playing: %s\n", argv[1]);
  gst_element_set_state (pipeline, GST_STATE_PLAYING);


  /* Iterate */
  g_print ("Running...\n");
  g_main_loop_run (loop);


  /* Out of the main loop, clean up nicely */
  g_print ("Returned, stopping playback\n");
  gst_element_set_state (pipeline, GST_STATE_NULL);

  g_print ("Deleting pipeline\n");
  gst_object_unref (GST_OBJECT (pipeline));
  g_source_remove (bus_watch_id);
  g_main_loop_unref (loop);

  return 0;
}

    

