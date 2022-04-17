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

import com.quyhoangtrinhvuteam.pbl5.R;
import com.quyhoangtrinhvuteam.pbl5.databinding.ActivityHelloBinding;

public class HelloActivity extends AppCompatActivity {

    ActivityHelloBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityHelloBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());


        checkFocusChange();
        checkSeri();
        checkPass();
        checkNewPass();

    }

    private void checkFocusChange() {
        binding.inputKey.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if (b) {
                    focusEditText();
                }
            }
        });

        binding.inputKeyPass.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if (b) {
                    focusEditText();
                }
            }
        });

        binding.inputKeyNewPass.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if (b) {
                    focusEditText();
                }
            }
        });
    }


    private void checkSeri() {
        binding.inputKey.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

                if (charSequence.toString().equals("quy")) {
                    binding.imgCheck.setVisibility(View.VISIBLE);
                    binding.layoutPass.setVisibility(View.VISIBLE);
                    binding.layoutPass.setAlpha(0.0f);
                    binding.layoutPass.animate()
                            .translationYBy(binding.layoutPass.getHeight() * -1)
                            .translationY(0)
                            .alpha(1.0f)
                            .setDuration(600)
                            .setListener(null);
                    binding.inputKeyPass.requestFocus();
                } else {
                    binding.imgCheck.setVisibility(View.GONE);
                    if (binding.layoutPass.getVisibility() == View.VISIBLE) {
                        String s = binding.inputKeyPass.getText().toString();
                        binding.inputKeyPass.setText(" " + s + " ");
                        binding.layoutPass.animate()
                                .translationYBy(binding.layoutPass.getHeight())
                                .translationY(0)
                                .setDuration(600)
                                .alpha(0f)
                                .setListener(new AnimatorListenerAdapter() {
                                    @Override
                                    public void onAnimationEnd(Animator animation) {
                                        super.onAnimationEnd(animation);
                                        binding.layoutPass.setVisibility(View.GONE);
                                        binding.layoutNewPass.setVisibility(View.GONE);
                                        binding.inputKeyNewPass.setText("");
                                        binding.inputKeyPass.setText("");
                                    }
                                });
                    }

                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    private void checkPass() {
        binding.inputKeyPass.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

                if (charSequence.toString().equals("quy")) {
                    binding.imgCheckPass.setVisibility(View.VISIBLE);
                    binding.layoutNewPass.setVisibility(View.VISIBLE);
                    binding.layoutNewPass.setAlpha(0.0f);
                    binding.layoutNewPass.animate()
                            .translationYBy(binding.layoutNewPass.getHeight() * -1)
                            .translationY(0)
                            .alpha(1.0f)
                            .setDuration(600)
                            .setListener(null);
                    binding.inputKeyNewPass.requestFocus();
                } else {
                    binding.imgCheckPass.setVisibility(View.GONE);
                    if (binding.layoutNewPass.getVisibility() == View.VISIBLE) {

                        binding.layoutNewPass.animate()
                                .translationYBy(binding.layoutNewPass.getHeight())
                                .translationY(0)
                                .setDuration(600)
                                .alpha(0f)
                                .setListener(new AnimatorListenerAdapter() {
                                    @Override
                                    public void onAnimationEnd(Animator animation) {
                                        super.onAnimationEnd(animation);
                                        binding.layoutNewPass.setVisibility(View.GONE);
                                        binding.inputKeyNewPass.setText("");
                                    }
                                });
                    }
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    private void checkNewPass() {
        binding.inputKeyNewPass.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                if(charSequence.toString().length() > 5){
                    binding.btnSubmit.setEnabled(true);
                    binding.btnSubmit.setBackgroundColor(Color.parseColor("#3B8F3E"));
                    binding.btnSubmit.setTextColor(Color.WHITE);
                }else{
                    binding.btnSubmit.setEnabled(false);
                    binding.btnSubmit.setBackgroundColor(Color.parseColor("#989898"));
                    binding.btnSubmit.setTextColor(Color.parseColor("#CDCDCD"));
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    private void focusEditText() {
        View lastChild = binding.scrollLayout.getChildAt(binding.scrollLayout.getChildCount() - 1);
        int bottom = lastChild.getBottom() + binding.scrollLayout.getPaddingBottom();
        int sy = binding.scrollLayout.getScrollY();
        int sh = binding.scrollLayout.getHeight();
        int delta = bottom - (sy + sh);

        binding.scrollLayout.smoothScrollBy(0, delta);
    }
}