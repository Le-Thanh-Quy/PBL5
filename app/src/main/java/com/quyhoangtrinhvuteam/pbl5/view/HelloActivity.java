package com.quyhoangtrinhvuteam.pbl5.view;

import androidx.appcompat.app.AppCompatActivity;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.view.animation.TranslateAnimation;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.ValueEventListener;
import com.quyhoangtrinhvuteam.pbl5.R;
import com.quyhoangtrinhvuteam.pbl5.databinding.ActivityHelloBinding;
import com.quyhoangtrinhvuteam.pbl5.model.FirebaseDB;

public class HelloActivity extends AppCompatActivity {

    ActivityHelloBinding binding;
    
    private String serialCode;
    private String pinCode;
    private String newPinCode;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityHelloBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());


        checkFocusChange();
        serialTextChange();
        PinTextChage();
        checkNewPin();
        login();
    }

    private void login() {
        binding.btnSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(HelloActivity.this, "Main App", Toast.LENGTH_SHORT).show();
            }
        });
    }

    // cuộn xuống cuối cùng khi focus vào một trường edittext
    private void checkFocusChange() {
        binding.inputSerial.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if (b) {
                    focusEditText();
                }
            }
        });

        binding.inputPin.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if (b) {
                    focusEditText();
                }
            }
        });

        binding.inputNewPin.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if (b) {
                    focusEditText();
                }
            }
        });
    }

    
    private void serialTextChange() {
        binding.inputSerial.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if (charSequence.length() == 10) {
                    checkSerialCorrect(charSequence.toString());
                } else {
                    binding.imgCheckSerial.setVisibility(View.GONE);
                    hideInputPin();
                }


            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }


    // kiểm tra serial có tồn tại hay không
    private void checkSerialCorrect(String serial) {
        FirebaseDB.getInstance().reference.child(serial).addListenerForSingleValueEvent(new ValueEventListener() {
            @SuppressLint("UseCompatLoadingForDrawables")
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                if (dataSnapshot.exists()) {
                    serialCode = serial;
                    binding.imgCheckSerial.setImageDrawable(getResources().getDrawable(R.drawable.ic_baseline_check_24));
                    showInputPin();
                } else {
                    binding.imgCheckSerial.setImageDrawable(getResources().getDrawable(R.drawable.ic_baseline_close_24));
                    binding.imgCheckSerial.setVisibility(View.VISIBLE);
                    hideInputPin();
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                throw databaseError.toException();
            }
        });
    }
    
    private void showInputPin() {
        binding.imgCheckSerial.setVisibility(View.VISIBLE);
        binding.layoutPin.setVisibility(View.VISIBLE);
        binding.layoutPin.setAlpha(0.0f);
        binding.layoutPin.animate()
                .translationYBy(binding.layoutPin.getHeight() * -1)
                .translationY(0)
                .alpha(1.0f)
                .setDuration(600)
                .setListener(null);
        binding.inputPin.requestFocus();
    }

    private  void hideInputPin() {

        if (binding.layoutPin.getVisibility() == View.VISIBLE) {
            String s = binding.inputPin.getText().toString();
            binding.inputPin.setText(" " + s + " ");
            binding.layoutPin.animate()
                    .translationYBy(binding.layoutPin.getHeight())
                    .translationY(0)
                    .setDuration(600)
                    .alpha(0f)
                    .setListener(new AnimatorListenerAdapter() {
                        @Override
                        public void onAnimationEnd(Animator animation) {
                            super.onAnimationEnd(animation);
                            binding.layoutPin.setVisibility(View.GONE);
                            binding.layoutNewPin.setVisibility(View.GONE);
                            binding.inputNewPin.setText("");
                            binding.inputPin.setText("");
                        }
                    });
        }
    }

    
    private void PinTextChage() {
        binding.inputPin.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if(charSequence.length() == 10) {
                    checkInputPin(charSequence.toString());
                } else {
                    binding.imgCheckPin.setVisibility(View.GONE);
                    hideInputNewPin();
                }

            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    // kiểm tra mã pin có chính xác hay không
    private void checkInputPin(String pin) {
        FirebaseDB.getInstance().reference.child(serialCode).child("Pin").addListenerForSingleValueEvent(new ValueEventListener() {
            @SuppressLint("UseCompatLoadingForDrawables")
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                if (pin.equals(dataSnapshot.getValue(String.class))) {
                    pinCode = pin;
                    binding.imgCheckPin.setImageDrawable(getResources().getDrawable(R.drawable.ic_baseline_check_24));
                    showInputNewPin();
                } else {
                    binding.imgCheckPin.setImageDrawable(getResources().getDrawable(R.drawable.ic_baseline_close_24));
                    binding.imgCheckPin.setVisibility(View.VISIBLE);
                    hideInputNewPin();
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                throw databaseError.toException();
            }
        });
    }


    private void showInputNewPin() {
        binding.imgCheckPin.setVisibility(View.VISIBLE);
        binding.layoutNewPin.setVisibility(View.VISIBLE);
        binding.layoutNewPin.setAlpha(0.0f);
        binding.layoutNewPin.animate()
                .translationYBy(binding.layoutNewPin.getHeight() * -1)
                .translationY(0)
                .alpha(1.0f)
                .setDuration(600)
                .setListener(null);
        binding.inputNewPin.requestFocus();
    }

    private void hideInputNewPin() {
        if (binding.layoutNewPin.getVisibility() == View.VISIBLE) {

            binding.layoutNewPin.animate()
                    .translationYBy(binding.layoutNewPin.getHeight())
                    .translationY(0)
                    .setDuration(600)
                    .alpha(0f)
                    .setListener(new AnimatorListenerAdapter() {
                        @Override
                        public void onAnimationEnd(Animator animation) {
                            super.onAnimationEnd(animation);
                            binding.layoutNewPin.setVisibility(View.GONE);
                            binding.inputNewPin.setText("");
                            binding.inputNewPin.setError(null);
                        }
                    });
        }
    }

    // kiểm tra tính bảo mật của mã pin mới
    private void checkNewPin() {
        binding.inputNewPin.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if (isStrong(charSequence.toString())) {
                    binding.btnSubmit.setEnabled(true);
                    binding.btnSubmit.setBackgroundColor(Color.parseColor("#3B8F3E"));
                    binding.btnSubmit.setTextColor(Color.WHITE);
                    binding.imgCheckNewPin.setImageDrawable(getResources().getDrawable(R.drawable.ic_baseline_check_24));
                    binding.imgCheckNewPin.setVisibility(View.VISIBLE);
                } else {
                    binding.btnSubmit.setEnabled(false);
                    binding.btnSubmit.setBackgroundColor(Color.parseColor("#989898"));
                    binding.btnSubmit.setTextColor(Color.parseColor("#CDCDCD"));
                    binding.imgCheckNewPin.setImageDrawable(getResources().getDrawable(R.drawable.ic_baseline_close_24));
                    binding.imgCheckNewPin.setVisibility(View.VISIBLE);

                }

                if(charSequence.length() < 10) {
                    binding.imgCheckNewPin.setVisibility(View.GONE);
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    // 10 ký tự bao gồm số, chữ cái, chữ in hoa
    private boolean isStrong(String Pinword) {
        String regexp = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{10}$";
        return Pinword.matches(regexp);
    }


    // cuộn xuống cuối màn hình
    private void focusEditText() {
        View lastChild = binding.scrollLayout.getChildAt(binding.scrollLayout.getChildCount() - 1);
        int bottom = lastChild.getBottom() + binding.scrollLayout.getPaddingBottom();
        int sy = binding.scrollLayout.getScrollY();
        int sh = binding.scrollLayout.getHeight();
        int delta = bottom - (sy + sh);

        binding.scrollLayout.smoothScrollBy(0, delta);
    }
}