package com.quyhoangtrinhvuteam.pbl5.view;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
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
        
    }

    private void checkFocusChange() {
        binding.inputKey.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b){
                    focusEditText();
                }
            }
        });

        binding.inputKeyPass.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b){
                    focusEditText();
                }
            }
        });

        binding.inputKeyNewPass.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View view, boolean b) {
                if(b){
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

                if(charSequence.toString().equals("taotenquy")) {
                    binding.imgCheck.setVisibility(View.VISIBLE);
                    binding.layoutPass.setVisibility(View.VISIBLE);
                    binding.inputKeyPass.requestFocus();
                }else{
                    binding.imgCheck.setVisibility(View.INVISIBLE);
                    binding.layoutPass.setVisibility(View.INVISIBLE);
                    binding.layoutNewPass.setVisibility(View.INVISIBLE);
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

                if(charSequence.toString().equals("quy")) {
                    binding.imgCheckPass.setVisibility(View.VISIBLE);
                    binding.layoutNewPass.setVisibility(View.VISIBLE);
                    binding.inputKeyNewPass.requestFocus();
                }else{
                    binding.imgCheckPass.setVisibility(View.INVISIBLE);
                    binding.layoutNewPass.setVisibility(View.INVISIBLE);
                }
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });
    }

    private void focusEditText(){
        View lastChild = binding.scrollLayout.getChildAt(binding.scrollLayout.getChildCount() - 1);
        int bottom = lastChild.getBottom() + binding.scrollLayout.getPaddingBottom();
        int sy = binding.scrollLayout.getScrollY();
        int sh = binding.scrollLayout.getHeight();
        int delta = bottom - (sy + sh);

        binding.scrollLayout.smoothScrollBy(0, delta);
    }
}