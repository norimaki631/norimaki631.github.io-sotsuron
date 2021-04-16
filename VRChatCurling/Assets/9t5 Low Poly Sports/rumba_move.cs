using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class rumba_move : MonoBehaviour
{
    public GameObject red1;
    public GameObject red2;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {


        Vector3 r1 = red1.transform.position;
        Vector3 t1 = this.transform.position;
        t1.x = -0.55f;
        t1.y = 1.28f;
        t1.z = r1.z ;
        this.transform.position = t1;
    }
}
