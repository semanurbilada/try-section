/*   
- kısa süreli bir unity projesi içindi
- vscode ile yazıldı (unity default)

-> Unity'de tasarlanan ortamda;
- tarımsal aracı (İKA) tarlada hareket ettirmek için,
- ve bitkiyi (yabani otu), araç hareket ettikçe tarlaya eklemesi için.
*/
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//hatayı çözmek için eklendi
using.System;

public class creatingObjects : MonoBehaviour
{

    public Transform tarla;
    public GameObject yabani_ot;

    //oyun başladığında çalışması için
    void Start()
    {
        //Instantiate the gaming object (yabani ot)
        Instantiate(yabani_ot, tarla.position, tarla.rotation);

    } //void start

} //public class
