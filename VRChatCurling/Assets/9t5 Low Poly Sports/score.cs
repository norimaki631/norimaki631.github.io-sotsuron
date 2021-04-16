using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class score : MonoBehaviour
{
    public int RedScore;
    public int BlueScore;
    public int round;
    public Text ScoreText;
    public Text Round;
    public GameObject red1;
    public GameObject red2;
    public GameObject blue1;
    public GameObject blue2;

    bool One;

    // Start is called before the first frame update
    void Start()
    {
        One = true;
        Vector3 b1 = blue1.transform.position;
        Vector3 b2 = blue2.transform.position;
        b1.x = 2.8f;
        b1.y = 1.161602f;
        b1.z = 60.48f;
        b2.x = -5.55f;
        b2.y = 1.161602f;
        b2.z = 54.12f;
        blue1.transform.position = b1;
        blue2.transform.position = b2;
        round = 1;
        Round.text = round.ToString();
        Invoke("Round2", 25);
        Invoke("Blue2", 25);
        Invoke("Round3", 70);
        Invoke("Blue2", 70);
    }

    // Update is called once per frame
    void Update()
    {
        Rigidbody rb = red2.transform.GetComponent<Rigidbody>();
        float velocity = rb.velocity.magnitude;

        if (One & velocity == 0)
        {
            Finish();
            Debug.Log(RedScore.ToString() + "-" + BlueScore.ToString());
            ScoreText.text = RedScore.ToString() + "-" + BlueScore.ToString();
            One = false;
        }

        if (One & velocity == 0)
        {
            //round += 1;
            //Round.text = round.ToString();

            Finish();
            Debug.Log(RedScore.ToString() + "-" + BlueScore.ToString());
            ScoreText.text = RedScore.ToString() + "-" + BlueScore.ToString();
            One = false;
        }

    }

    void Round2()
    {
        round = 2;
        Round.text = round.ToString();
    }
    
    void Blue2()
    {

        Vector3 b1 = blue1.transform.position;
        Vector3 b2 = blue2.transform.position;
        b1.x = 2.8f;
        b1.y = 1.161602f;
        b1.z = 58.83f;
        b2.x = -5.55f;
        b2.y = 1.161602f;
        b2.z = 51.35f;
        blue1.transform.position = b1;
        blue2.transform.position = b2;


    }

    void Round3()
    {
        round = 3;
        Round.text = round.ToString();
    }

    void Blue3()
    {
        Vector3 b1 = blue1.transform.position;
        Vector3 b2 = blue2.transform.position;
        b1.x = 2.8f;
        b1.y = 1.161602f;
        b1.z = 69.08f;
        b2.x = -5.55f;
        b2.y = 1.161602f;
        b2.z = 43.52f;
        blue1.transform.position = b1;
        blue2.transform.position = b2;


    }

    void Finish()
    {
        Vector3 center = new Vector3(9.9f, 3.753568f, -2.39f);
        Vector3 edge = new Vector3(9.9f, 3.753568f, -3.532f);
        Vector3 r1 = red1.transform.position;
        Vector3 r2 = red2.transform.position;
        Vector3 b1 = blue1.transform.position;
        Vector3 b2 = blue2.transform.position;
        float r1d = (r1 - center).magnitude;
        float r2d = (r2 - center).magnitude;
        float b1d = (b1 - center).magnitude;
        float b2d = (b2 - center).magnitude;
        float diameter = (edge - center).magnitude;

        Debug.Log("r1:" + r1d.ToString() + " r2:" + r2d.ToString() + " b1:" + b1d.ToString() + " b2:" + b2d.ToString());


        if (Mathf.Min(r1d,r2d) < Mathf.Min(b1d, b2d) & Mathf.Min(r1d,r2d) < diameter)
        {
            BlueScore += 0;
            if (r1d < Mathf.Min(b1d, b2d) & r2d < Mathf.Min(b1d, b2d))
            {
                RedScore += 2;
            }
            else if (r1d < Mathf.Min(b1d, b2d) | r2d < Mathf.Min(b1d, b2d))
            {
                RedScore += 1;
            } 
        }

        if (Mathf.Min(b1d, b2d) < Mathf.Min(r1d, r2d) & Mathf.Min(b1d, b2d) < diameter)
        {
            RedScore += 0;
            if (b1d < Mathf.Min(r1d, r2d) & b2d < Mathf.Min(r1d, r2d))
            {
                BlueScore += 2;
            }
            else if (b1d < Mathf.Min(r1d, r2d) | b2d < Mathf.Min(r1d, r2d))
            {
                BlueScore += 1;
            } 
        }

        if (Mathf.Min(r1d, r2d) > diameter & Mathf.Min(b1d, b2d) > diameter)
        {
            BlueScore += 0;
            RedScore += 0;
        }
    }
}
