Shader "A3/UnlitReversible"
{
	Properties
	{
		_MainTex("MainTex", 2D) = "white" {}
		_BackTex("BackTex", 2D) = "white" {}
		_Color("Color", Color) = (1,1,1,1)
		_Cutoff("Alpha Cutoff", Range(0,1)) = 0.5
		[Space]
		// Blending state
		_Mode ("Mode", Float) = 0.0
		[Enum(UnityEngine.Rendering.BlendMode)] _SrcBlend ("SrcBlend", Float) = 1.0
		[Enum(UnityEngine.Rendering.BlendMode)] _DstBlend ("DstBlend", Float) = 0.0
		_ZWrite ("ZWrite", Float) = 1.0
	}

	SubShader
	{
		Tags
		{
			"RenderType" = "Opaque"
		}

		Pass
		{
			Cull Off
			CGPROGRAM
			#include "UnityCG.cginc"
			uniform sampler2D _MainTex; uniform float4 _MainTex_ST;
			uniform sampler2D _BackTex; uniform float4 _BackTex_ST;
			uniform float _Cutoff;
			uniform float4 _Color;
			#pragma vertex vert
			#pragma fragment frag
			struct VertexOutput
			{
				float4 pos : SV_POSITION;
				float2 uv0 : TEXCOORD0;
			};
			VertexOutput vert(appdata_base v)
			{
				VertexOutput o;
				o.uv0 = v.texcoord;
				o.pos = UnityObjectToClipPos(v.vertex);
				return o;
			}
			fixed4 frag (VertexOutput i, fixed facing : VFACE) : SV_Target
			{
				float4 baseColor;
				if(facing > 0)baseColor = tex2D(_MainTex,TRANSFORM_TEX(i.uv0, _MainTex));
				else baseColor = tex2D(_BackTex,TRANSFORM_TEX(float2(1-i.uv0.x, i.uv0.y), _BackTex));
				clip (baseColor.a - _Cutoff);
				return baseColor;
			}
			ENDCG
		}
	}
	FallBack "Diffuse"
}
