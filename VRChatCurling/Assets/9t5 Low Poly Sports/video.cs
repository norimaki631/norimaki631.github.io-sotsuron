using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Video;

public class video : MonoBehaviour
{
    public VideoPlayer videoplayer;

    // Start is called before the first frame update
    void Start()
    {
        videoplayer.time = 0f;
        videoplayer.Play();
        //videoplayer.time = 2f;
        //videoplayer.Pause();
        //double length = videoplayer.clip.length;
        //Debug.Log(length.ToString());
    }

    // Update is called once per frame
    void Update()
    {
        //Rigidbody rb = this.transform.GetComponent<Rigidbody>();
        //float velocity = rb.velocity.magnitude;
        //if(velocity == 0)
        //{
        //    videoplayer.time = 15f;
        //    videoplayer.Play();
        //}
    }
}
