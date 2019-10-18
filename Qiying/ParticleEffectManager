void Start () {  
        EffectManager = GameObject.Find("EffectManager");  
        PowerCallParticle = Resources.Load("Effect/Power_Call");  
    }  


public void PowerParticle(string powerName,int powerTime) {  
        GameObject PowerCellObj = Instantiate(PowerCallParticle) as GameObject;  
        PowerCellObj.SetActive(true);  
        PowerCellObj.transform.parent = EffectManager.transform;  
        var powerDes = PowerCellObj.transform.Find("Des/PowerName");  
        powerDes.GetComponent<TextMesh>().text = powerName;  
        GameObject PowerParticle_left = PowerCellObj.transform.Find("Particle_left").gameObject;  
        GameObject PowerParticle_right = PowerCellObj.transform.Find("Particle_right").gameObject;  
        Destroy(PowerParticle_left, powerTime - 1);  
        Destroy(PowerParticle_right, powerTime - 1);  
        Destroy(PowerCellObj, powerTime);  
    }  
