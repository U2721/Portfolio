using System;
 public void BackgroundRotationAnimation()
     {  
         animName = "BackgroundRotation";  
         isClockwise = !isClockwise;  
         if (isClockwise)  
         {  
             animRotaion[animName].speed = -1;  
         }  
         else  
         {  
             animRotaion[animName].speed = 1;  
         }  
         animRotaion.Play(animName);  
   
     }  

 public void ChangeEmissionMap(MeshRenderer[] meshRenderers)
     {  
         for (int i = 0; i<meshRenderers.Length; i++)  
         {  
             meshRenderers[i].materials[0].SetTexture("_EmissionMap", changedMap);  
             meshRenderers[i].materials[0].SetColor("_EmissionColor", new Color(0, 1, 1));  
         }  
     }  
   
     public void ResetEmissionMap(MeshRenderer[] meshRenderers)
     {  
         for (int i = 0; i<meshRenderers.Length; i++)  
         {  
             meshRenderers[i].materials[0].SetTexture("_EmissionMap", originalMap);  
             meshRenderers[i].materials[0].SetColor("_EmissionColor", new Color(1, 1, 0.3372549f));  
         }  
     }  

 public void ChangeTrayColor(MeshRenderer[] meshRenderers)
     {  
         for (int i = 0; i<meshRenderers.Length; i++)  
         {  
             meshRenderers[i].materials[0].SetColor("_EmissionColor", new Color(1, 0.688f, 0.341f));  
         }  
     }  
   
     public void ResetTrayColor(MeshRenderer[] meshRenderers)
     {  
         for (int i = 0; i<meshRenderers.Length; i++)  
         {  
             meshRenderers[i].materials[0].SetColor("_EmissionColor", new Color(0, 1.223528f, 6));  
         }  
     }  

