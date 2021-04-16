using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class broom_controll : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //if (Input.GetKey(KeyCode.LeftArrow))
        //{
        //    this.transform.Translate(0.0f, 0.0f, -0.1f);
        //}

        //if (Input.GetKey(KeyCode.RightArrow))
        //{
        //    this.transform.Translate(0.0f, 0.0f, 0.1f);
        //}

        //if (Input.GetKey(KeyCode.UpArrow))
        //{
        //    this.transform.Translate(-0.1f, 0.0f, 0.0f);
        //}

        //if (Input.GetKey(KeyCode.DownArrow))
        //{
        //    this.transform.Translate(0.1f, 0.0f, 0.0f);
        //}
    }


    void OnMouseDrag()
    {
        Vector3 objectPointInScreen
            = Camera.main.WorldToScreenPoint(this.transform.position);

        Vector3 mousePointInScreen
            = new Vector3(Input.mousePosition.x,
                          Input.mousePosition.y,
                          objectPointInScreen.z);

        Vector3 mousePointInWorld = Camera.main.ScreenToWorldPoint(mousePointInScreen);
        mousePointInWorld.z = this.transform.position.z;
        this.transform.position = mousePointInWorld;
    }
}
