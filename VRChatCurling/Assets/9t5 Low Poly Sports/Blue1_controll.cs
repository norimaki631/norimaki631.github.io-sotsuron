using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Blue1_controll : MonoBehaviour
{
    public PhysicMaterial pm;
    public GameObject broom;

    // Start is called before the first frame update
    void Start()
    {
        pm.dynamicFriction = 0.05f;
    }

    // Update is called once per frame
    void Update()
    {
        Rigidbody rb = broom.transform.GetComponent<Rigidbody>();
        float velocity = rb.velocity.magnitude;

        float Distance = (broom.transform.position - this.transform.position).magnitude;


        if (Distance <= 5.0f)
        {
            pm.dynamicFriction -= velocity;
        }
    }
}
