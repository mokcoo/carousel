PGDMP         6            	    {           carousel     12.16 (Debian 12.16-1.pgdg120+1)    15.3 (    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    17265    carousel    DATABASE     s   CREATE DATABASE carousel WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE carousel;
                kong    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                kong    false            �           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   kong    false    6            �            1259    17428    slider    TABLE     8   CREATE TABLE public.slider (
    id integer NOT NULL
);
    DROP TABLE public.slider;
       public         heap    kong    false    6            �            1259    17426    slider_id_seq    SEQUENCE     �   CREATE SEQUENCE public.slider_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.slider_id_seq;
       public          kong    false    203    6            �           0    0    slider_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.slider_id_seq OWNED BY public.slider.id;
          public          kong    false    202            �            1259    17461 
   sliderdata    TABLE     z   CREATE TABLE public.sliderdata (
    id integer NOT NULL,
    slider_id integer NOT NULL,
    item_id integer NOT NULL
);
    DROP TABLE public.sliderdata;
       public         heap    kong    false    6            �            1259    17459    sliderdata_id_seq    SEQUENCE     �   CREATE SEQUENCE public.sliderdata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.sliderdata_id_seq;
       public          kong    false    6    209            �           0    0    sliderdata_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.sliderdata_id_seq OWNED BY public.sliderdata.id;
          public          kong    false    208            �            1259    17436    sliderimage    TABLE     g   CREATE TABLE public.sliderimage (
    id integer NOT NULL,
    link character varying(200) NOT NULL
);
    DROP TABLE public.sliderimage;
       public         heap    kong    false    6            �            1259    17434    sliderimage_id_seq    SEQUENCE     �   CREATE SEQUENCE public.sliderimage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.sliderimage_id_seq;
       public          kong    false    205    6            �           0    0    sliderimage_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.sliderimage_id_seq OWNED BY public.sliderimage.id;
          public          kong    false    204            �            1259    17444 
   slideritem    TABLE     $  CREATE TABLE public.slideritem (
    id integer NOT NULL,
    title character varying(200) NOT NULL,
    description character varying(200) NOT NULL,
    "buttonText" character varying(200) NOT NULL,
    component character varying(200) NOT NULL,
    "backgroundImage_id" integer NOT NULL
);
    DROP TABLE public.slideritem;
       public         heap    kong    false    6            �            1259    17442    slideritem_id_seq    SEQUENCE     �   CREATE SEQUENCE public.slideritem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.slideritem_id_seq;
       public          kong    false    207    6            �           0    0    slideritem_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.slideritem_id_seq OWNED BY public.slideritem.id;
          public          kong    false    206            5           2604    17431 	   slider id    DEFAULT     f   ALTER TABLE ONLY public.slider ALTER COLUMN id SET DEFAULT nextval('public.slider_id_seq'::regclass);
 8   ALTER TABLE public.slider ALTER COLUMN id DROP DEFAULT;
       public          kong    false    202    203    203            8           2604    17464    sliderdata id    DEFAULT     n   ALTER TABLE ONLY public.sliderdata ALTER COLUMN id SET DEFAULT nextval('public.sliderdata_id_seq'::regclass);
 <   ALTER TABLE public.sliderdata ALTER COLUMN id DROP DEFAULT;
       public          kong    false    209    208    209            6           2604    17439    sliderimage id    DEFAULT     p   ALTER TABLE ONLY public.sliderimage ALTER COLUMN id SET DEFAULT nextval('public.sliderimage_id_seq'::regclass);
 =   ALTER TABLE public.sliderimage ALTER COLUMN id DROP DEFAULT;
       public          kong    false    204    205    205            7           2604    17447    slideritem id    DEFAULT     n   ALTER TABLE ONLY public.slideritem ALTER COLUMN id SET DEFAULT nextval('public.slideritem_id_seq'::regclass);
 <   ALTER TABLE public.slideritem ALTER COLUMN id DROP DEFAULT;
       public          kong    false    207    206    207            �          0    17428    slider 
   TABLE DATA           $   COPY public.slider (id) FROM stdin;
    public          kong    false    203   �*       �          0    17461 
   sliderdata 
   TABLE DATA           <   COPY public.sliderdata (id, slider_id, item_id) FROM stdin;
    public          kong    false    209   �*       �          0    17436    sliderimage 
   TABLE DATA           /   COPY public.sliderimage (id, link) FROM stdin;
    public          kong    false    205   �*       �          0    17444 
   slideritem 
   TABLE DATA           k   COPY public.slideritem (id, title, description, "buttonText", component, "backgroundImage_id") FROM stdin;
    public          kong    false    207   �+       �           0    0    slider_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.slider_id_seq', 5, true);
          public          kong    false    202            �           0    0    sliderdata_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.sliderdata_id_seq', 10, true);
          public          kong    false    208            �           0    0    sliderimage_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.sliderimage_id_seq', 10, true);
          public          kong    false    204            �           0    0    slideritem_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.slideritem_id_seq', 10, true);
          public          kong    false    206            :           2606    17433    slider slider_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.slider
    ADD CONSTRAINT slider_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.slider DROP CONSTRAINT slider_pkey;
       public            kong    false    203            B           2606    17466    sliderdata sliderdata_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.sliderdata
    ADD CONSTRAINT sliderdata_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.sliderdata DROP CONSTRAINT sliderdata_pkey;
       public            kong    false    209            <           2606    17441    sliderimage sliderimage_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.sliderimage
    ADD CONSTRAINT sliderimage_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.sliderimage DROP CONSTRAINT sliderimage_pkey;
       public            kong    false    205            ?           2606    17452    slideritem slideritem_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.slideritem
    ADD CONSTRAINT slideritem_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.slideritem DROP CONSTRAINT slideritem_pkey;
       public            kong    false    207            @           1259    17478    sliderdata_item_id    INDEX     L   CREATE INDEX sliderdata_item_id ON public.sliderdata USING btree (item_id);
 &   DROP INDEX public.sliderdata_item_id;
       public            kong    false    209            C           1259    17477    sliderdata_slider_id    INDEX     P   CREATE INDEX sliderdata_slider_id ON public.sliderdata USING btree (slider_id);
 (   DROP INDEX public.sliderdata_slider_id;
       public            kong    false    209            =           1259    17458    slideritem_backgroundImage_id    INDEX     f   CREATE INDEX "slideritem_backgroundImage_id" ON public.slideritem USING btree ("backgroundImage_id");
 3   DROP INDEX public."slideritem_backgroundImage_id";
       public            kong    false    207            E           2606    17472 "   sliderdata sliderdata_item_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sliderdata
    ADD CONSTRAINT sliderdata_item_id_fkey FOREIGN KEY (item_id) REFERENCES public.slideritem(id);
 L   ALTER TABLE ONLY public.sliderdata DROP CONSTRAINT sliderdata_item_id_fkey;
       public          kong    false    2879    207    209            F           2606    17467 $   sliderdata sliderdata_slider_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sliderdata
    ADD CONSTRAINT sliderdata_slider_id_fkey FOREIGN KEY (slider_id) REFERENCES public.slider(id);
 N   ALTER TABLE ONLY public.sliderdata DROP CONSTRAINT sliderdata_slider_id_fkey;
       public          kong    false    2874    209    203            D           2606    17453 -   slideritem slideritem_backgroundImage_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.slideritem
    ADD CONSTRAINT "slideritem_backgroundImage_id_fkey" FOREIGN KEY ("backgroundImage_id") REFERENCES public.sliderimage(id);
 Y   ALTER TABLE ONLY public.slideritem DROP CONSTRAINT "slideritem_backgroundImage_id_fkey";
       public          kong    false    2876    207    205            �      x�3�2�2�2����� *�      �   3   x���  ���&����A>�e�^vRC�*[S�S�RG��5��a�      �   y   x�����  г��'`0�/,��Xf6�h�V���7����jݾ�㐥��d�wDTH$c���Q���Y�IEl:�9���%`1�B�.���u�MX�}f�=��`���ɺO��)!��!�x      �   t   x���M
� ���a�	�;Bw"�"Hl����\��a��e��&�٣_�0łY�6��i�v�θ��gE��O�_k�����"幺�����*幺����5����S��p��~�     