package com.quyhoangtrinhvuteam.pbl5.model;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

public class FirebaseDB {
    private FirebaseDatabase database;
    public DatabaseReference reference;
    private FirebaseStorage storage;
    public StorageReference storageReference;

    private static FirebaseDB instance;

    public static FirebaseDB getInstance() {
        if (instance == null) {
            instance = new FirebaseDB();
        }

        return instance;
    }
    public FirebaseDB() {
        database = FirebaseDatabase.getInstance();
        reference = database.getReference();
        storage  = FirebaseStorage.getInstance();
        storageReference = storage.getReference();
    }


    //myRef.setValue("Hello, World!");
//
//
//        myRef.addValueEventListener(new ValueEventListener() {
//            @Override
//            public void onDataChange(DataSnapshot dataSnapshot) {
//                // This method is called once with the initial value and again
//                // whenever data at this location is updated.
//                String value = dataSnapshot.getValue(String.class);
//                Log.d("AAAA", "Value is: " + value);
//            }
//
//            @Override
//            public void onCancelled(DatabaseError error) {
//                // Failed to read value
//                Log.w("BBB", "Failed to read value.", error.toException());
//            }
//        });
//

//
//        Uri file = Uri.parse("android.resource://com.quyhoangtrinhvuteam.pbl5/" + R.drawable.imgabc);
//        StorageReference ref = storageRef.child("images/" + file.getLastPathSegment() + ".png");
//
//        UploadTask uploadTask = ref.putFile(file);
//
//        Task<Uri> urlTask = uploadTask.continueWithTask(new Continuation<UploadTask.TaskSnapshot, Task<Uri>>() {
//            @Override
//            public Task<Uri> then(@NonNull Task<UploadTask.TaskSnapshot> task) throws Exception {
//                if (!task.isSuccessful()) {
//                    throw task.getException();
//                }
//                return ref.getDownloadUrl();
//            }
//        }).addOnCompleteListener(new OnCompleteListener<Uri>() {
//            @Override
//            public void onComplete(@NonNull Task<Uri> task) {
//                if (task.isSuccessful()) {
//                    Uri downloadUri = task.getResult();
//                    Log.d("Uri", downloadUri.toString());
//                } else {
//                }
//            }
//        });

}
