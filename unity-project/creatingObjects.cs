/*   
- kısa süreli bir unity projesi için
- vscode ile yazıldı (unity default)

-> Unity'de tasarlanan ortamda;
- tarımsal aracı (İKA) tarlada hareket ettirmek için,
- ve bitkiyi (yabani otu), araç hareket ettikçe tarlaya eklemesi için.
*/
//hatayı çözmek için eklendi
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class creatingObjects : MonoBehaviour
{
    public Transform tarla;
    public GameObject yabani_ot;

    //oyun başladığında çalışması için
    void Start()
    {
        //Instantiate the gaming object (yabani ot)
        Instantiate(yabani_ot, tarla.position, tarla.rotation);

    } 
} 