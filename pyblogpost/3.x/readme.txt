����������������
(����ʽ��ȫ��Ĺ��߲ο��ĵ�����μ�������������������ʹ��˵����http://sinojelly.blog.51cto.com/479153/278444)

��Pythonд���������������������µĹ��ߣ��ֳ�pyBlogPost��
֧��һ���ϴ��������������
֧��ֻ��һ��ָ���ķ������ϴ�ͼƬ�������ط�ֱ��Ӧ�ã�
֧�ּ���ļ�/ͼƬ�Ƿ��и��£�ֻ�ϴ����µ��ļ�/ͼƬ������ÿ�θ������¶���������ϴ�����ͼƬ��

�����б�
===================
1��֧����WordPress��cnblogs�Ȳ��ͷ�����������ͼ�����¡�
2��֧��һ�������������������¡�
3��֧��ͨ��xml�ļ����÷�����������
4��֧�ַ���WizKnowedge���¡�
5��֧��ָ��һ�����ͷ������ϴ�ͼƬ����������ֱ�����ӡ�
6��֧��ÿ�����Ͷ������ϴ�ͼƬ��
7���������޸ĵ�ʱ��ֻ�����ѷ��������¡�
8���������޸ĵ�ʱ�򣬲�����Ҳ���������¡�
9��ͼƬҲ�������޸ĵ�ʱ�򣬲������ϴ�������ÿ�θ������¶�������ͼƬ���ϴ�һ�Ρ�
10��ͨ���˹����ϴ����ļ��̶����ӵ�ַ������WordPress���slug���������Զ���Ϊ����ʶ���Ӣ�Ļ���ƴ�������������֡���WK�Դ����ϴ��޴˹��ܣ�
11������MD5���Ƿ���ͬ�ж��ļ��Ƿ����޸ġ�
12��html�ļ�û�޸ģ�ֻ�޸�ͼƬ����ôͼƬ���ᵥ���ϴ���
13�������޸�MIME.xml��֧�ָ���ý���ļ����͡�
14��֧����ΪWizKnowedge����������ڵ�һ�η���ʱ����UUID��Ȼ����Ϊ�����µ�����Ψһ��ʾ��
15��֧���ϴ�ʱָ�����·��ࡣ


ʹ�÷���
===================
��Ҫ�Ȱ�װPython 3.1���ϰ汾�����Ұ�Python.exe����Ŀ¼���ӵ�path�����С�
1���޸������ļ�blogconfig.xml������Ϊ�Լ��Ĳ��ͷ��������˻�������
2���������python.exe blogpost.py categories html_file file_guid html_file2 file_guid2 ...
3����õ�ʹ�÷�������ΪWizKnowedge���ʹ�ã���ô��Ҫ��%USERPROFILE%\My Documents\My Knowledge\PluginsĿ¼�����µ�Ŀ¼��{A0D025CD-970A-4C62-97E4-5CF6F2C9DD6A}����
Ȼ��Ѵ�����С�https://pyblogpost.googlecode.com/hg/trunk/3.x"���д������ص���Ŀ¼�����´�WizKnowedge���Ϳ��Կ�������˵��ж���һ��������������������
ע����Ҫ���޸�blogconfig.xml�еķ��������ã��ٷ������¡�
3�����·���categories���԰�Ƕ��ŷָ��Ķ��������ɵ��ַ��������������ġ��÷�������ڷ��������Ѵ��ڣ�������Ч���ڿͻ��˲��ܴ������ࣨ��ΪMetaWeblog��֧�ֿͻ��˴���,��ȻWordPress����֧�֣�������ͨ��Ҳ���岻�󣩡�

˵����
1��file_guid��html�ļ���Ψһ����ʶ���룬����������ô�޸Ķ����ֲ��䣬Ҳ�������������ظ���guid����0ʱ�����߻��Զ�����һ�������ұ����ڹ���Ŀ¼�µ�lastpost_guid.ini��
2��Ϊ�����ҵ�ͼƬ·������������ļ�Ϊhtml����ô���й���ʱ�ĵ�ǰĿ¼Ӧ����html_file����Ŀ¼���ر�����html�ļ��������·������ͼƬ������¡�
   �����������ziw���������Զ���ѹ������ʱĿ¼���Ұѵ�ǰĿ¼�л�������ʱĿ¼��


�����ļ�
===================
�ļ�����blogconfig.xml
����Ҫ�������Ĳ��ͷ������������Ϣ��
ע�⣺
1��posturlҪָ��Ϊxmlrpc.php��metablogapi.aspx��RPC.ashx������·��������Ҫ���Լ��Ĳ����˻���·����
2���û�������������Ĳ����˻����û��������롣��live space���⣬�μ�����˵����
3��blog server name�����ظ���
���ݸ�ʽ���£�
<?xml version="1.0"?>
<config>
    <fileserver>  --- ָ�����ϴ�ͼƬ�ļ��ķ�����Ϊfileserver
        <name>blog.sinojelly.dreamhosters.com</name>
        <system>wordpress</system>
        <posturl>http://blog.sinojelly.dreamhosters.com/xmlrpc.php</posturl>
        <username>admin</username>
        <password>123456</password>
        <postblog>true</postblog>   --- �Ƿ񷢲����µ���blog, ����������Ҳ�Ͳ����ϴ�ͼƬ�����ļ���������������Ϊtrue��
        <media>2</media>   --- ��fileserver �ض�Ϊ2��������ʧȥ����
    </fileserver>
    <blog>  --- �����ж��<blog>�ڵ㣬�Ӷ��������ͷ�����־
        <name>sinojelly.20x.cc</name>
        <system>wordpress</system>
        <posturl>http://sinojelly.20x.cc/xmlrpc.php</posturl>
        <username>admin</username>
        <password>654321</password>
        <postblog>true</postblog>
        <media>0</media>  --- �Ƿ���˷������ϴ�ͼƬ��ý���ļ�(0--���ϴ�, 1--�ϴ���Զ��·��ֻ���ڱ����ͣ�2--�ϴ���Զ��·�����ں������в���)
    </blog>
</config>


�����ļ�
===================
Ĭ���ļ�����blogdata.xml
�������º���Զ����ɴ��ļ��������ֶ��༭�����������ºܶ࣬�����̫��Ӱ����Ч�ʣ����԰���ɾ��������������
<data>
    <html_file wk_file_guid="">
        <media>
            <file local_path="">
                <remote_path></remote_path>
                <file_hash></file_hash>
            </file>
        </media>
        <blog name="">
            <postid></postid>
            <file_hash></file_hash>  -- post file modify time
        </blog>
    </html_file>
<data>


LiveSpace
===================
Ϊ��ʹ��MetaWeblog API�༭Live space�ռ��еĲ������ݣ�������Ҫ�ڿռ�����E-mail�������ܣ������������֡�

����Ŀռ��е�Options->E-mail Publishingѡ���������
��E-mail�������ܣ���ѡ�� secred word�������֡�
�ڳ����л��õ��û��������룬�����Ŀռ��ַΪ�� oldname.spaces.live.com�����û�������oldname,���������live id�����������������õ�secred word,������live id�����롣


�ɸĽ���
===================
1������ʱ�������ͼƬ�ϴ�ʧ�ܣ��ϴ�ͬ��ͼƬWizKnowedge�Դ����Ҳ��ʧ�ܡ�
2��html�ļ������ǲ��õ��������ʽ��ʽ�����Կ�����lxml.html��������������һ���ƺ�û��ֱ���ṩ���media�б��Ľӿڡ���������Ҫ�Բ��󣬸Ľ�����������ʽ���˺ܶ�.*��Ч�ʺܸߣ�
3��http����ʹ�õı����ǹ̶�Ϊgb2312���ǿ����ã�


������ʷ  2010.2.21  V1.0.1
==========================
1��֧����WP��cnblogs��categories�����޸���Python xmlrpc�⣬���ֶ�tuple��list�Ĵ�������
2��֧�ַ���51CTO���¡�
3��֧��ͨ�ű��ı�����ڷ����������ļ�������(��encoding)��������Ϊgb2312��������ȷ֧��51CTO����𡣣�
4������������������vcategoriesѡ�true��ʾ��Ҫ�ӷ�������ȡcategories�������������������õķ���ȡ���������򲻻�ȡ��������categories��
5��֧��WK�����װ�����Ҹ���һ��Python31����ɫ�汾��


��Դ��Ŀ·����
http://code.google.com/p/pyblogpost/

�����飺
http://space.cnblogs.com/group/101223/

��ϵ���ߣ�
QQ: 2578717
MSN: sinojelly@msn.cn
email: sinojelly@163.com
����΢����http://t.sina.com.cn/sinojelly
�ҵĲ��ͣ�http://sinojelly.20x.cc
          http://sinojelly.blog.51cto.com/
          http://www.cnblogs.com/sinojelly/
��̸��ԣ�
��ӭ��λ����ʹ�ô˹��ߣ���ӭ����Ȥ�����Ѽ�������������������Ľ������лл��
2010.2.13��������ʮ�� - 2010.2.19�������ڼ䣬ÿ��11��00-4��00��û��ĳɼ�����д��������ߡ�
�����ֻ��������WizKnowedge�����չ���͹��ߵĹ��ܣ��Ӷ���������İ����ʼ�������ϣ����ѡ��Python��ʵ��������
�漰��������Ľ���������������ɹ�������������WordPress�������³ɹ���Ȼ��ʵ����һ��������̵ļ�ª���õİ汾��
��������������֧��ֻ������ͼƬ�ȹ��ܣ����ǲ������������д���о���Python��xml�����Ⱥܶ෽������ݣ���ѧ���á�
���ڵ����ڣ�����һ����������Ҫ��İ汾��
�ź�������ʱ�޷�֧���������͵Ĳ��ͣ�Python��xmlrpc�����ȱ���޷�֧�֣���Ҫ�Լ�ʵ�֣�����Python 3������֧��https��

