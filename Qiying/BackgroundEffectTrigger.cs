using System;
namespace code
 void Start()
{
    backGroundEffect = this.transform.GetComponentInParent<BackgroundEffect>();
    lightingRotation = GameObject.Find("Light/LightingChangable/LightingRotation");
    lightingShining = GameObject.Find("Light/LightingChangable/LightingShining");
    lightingRotationScript = lightingRotation.GetComponentInParent<LightEffect>();
          }  

  public void OnTriggerEnter(Collider other)
      {  
          if (other.gameObject.name == "RhyCollider")  
          {  
              int id;  
              id = other.gameObject.transform.parent.GetComponent<TheRhyInfo>().GetRhyID();  
              if (id % 10 == 0)  
              {  
                  StartCoroutine(WaitToTrigger(0.5f));  
             }  
             if (id % 2 == 0)  
             {  
                 lightingRotationScript.LightingShining(lightingRotation.GetComponentsInChildren<MeshRenderer>());  
             }  
             if(id % 5 == 0)  
             {  
                 lightingRotationScript.LightingShining(lightingShining.GetComponentsInChildren<MeshRenderer>());  
             }  
                   
         }  

  IEnumerator WaitToTrigger(float time)
      {  
          yield return new WaitForSeconds(time);      
          backGroundEffect.BackgroundRotationAnimation();  
      }  
