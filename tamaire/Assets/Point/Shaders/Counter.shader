Shader "A3/Counter"
{
	Properties
	{
		_MainTex("MainTex", 2D) = "white" {}
		_Cutoff("Alpha Cutoff", Range(0,1)) = 0.5
		[Space]
		_Digit("Digit", Int) = 3
		_Width("Width", Range(0,1)) = 0.3
		[Space]
		_Point("Point", Int) = 0
		[Space]
		//Blending state
		_Mode ("Mode", Float) = 0.0
		[Enum(UnityEngine.Rendering.BlendMode)] _SrcBlend ("SrcBlend", Float) = 1.0
		[Enum(UnityEngine.Rendering.BlendMode)] _DstBlend ("DstBlend", Float) = 0.0
		_ZWrite ("ZWrite", Float) = 1.0
	}
	SubShader
	{
		Tags
		{
			"RenderType" = "TransparentCutout"
		}
		Pass
		{
			Cull off
			ZWrite [_ZWrite]
			Tags { "LightMode" = "ForwardBase" }
			Blend [_SrcBlend] [_DstBlend]
			CGPROGRAM
			#include "UnityCG.cginc"
			uniform sampler2D _MainTex; uniform float4 _MainTex_ST;
			uniform fixed _Cutoff;
			uniform int _Digit;
			uniform fixed _Width;
			uniform int _Point;
			struct VertexOutput
			{
				float4 pos : SV_POSITION;
				fixed2 uv0 : TEXCOORD0;
				uint p : TEXCOORD1;
			};
			VertexOutput vert(appdata_base v)
			{
				VertexOutput o;
				o.uv0 = v.texcoord;
				o.pos = UnityObjectToClipPos(v.vertex);
				o.p = _Point;
				return o;
			}
			fixed4 frag (VertexOutput i, fixed facing : VFACE) : SV_Target
			{
				fixed4 baseColor = float4(0,0,0,0);
				fixed x = i.uv0.x;
				if(facing<0)x = 1-x;
				fixed numStep = 1.0/_Digit;
				fixed numRate = 0.1/_Width;	//1/Width/10(0~10の10枚)
				//得点
				uint p = i.p;
				fixed x2 = fmod(x,numStep);
				half power = pow(10,floor((1-x)/numStep));
				if(x2 < _Width)baseColor = tex2D(_MainTex,TRANSFORM_TEX(float2(x2*numRate+fmod(floor(p/power),10)*0.1, i.uv0.y), _MainTex));
				//透過
				clip (baseColor.a - _Cutoff);
				return baseColor;
			}
			#pragma vertex vert
			#pragma fragment frag
			ENDCG
		}
	}
	FallBack "Transparent/Cutout/Diffuse"
}
