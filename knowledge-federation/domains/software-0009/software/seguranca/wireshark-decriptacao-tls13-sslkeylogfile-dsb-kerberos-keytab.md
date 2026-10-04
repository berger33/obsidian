---
id: software.seguranca.tranche06.000555
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/wireshark/wireshark/master/README.md", "https://www.wireshark.org/docs/man-pages/tshark.html", "https://www.wireshark.org/docs/wsug_html_chunked/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Wireshark & `tshark`: Decriptação Passiva de Tráfego **TLS 1.2/1.3** (`SSLKEYLOGFILE` e `editcap --inject-secrets`) e **Kerberos** (`keytab`)

## Em uma frase
Com a adoção universal de *Perfect Forward Secrecy* (ECDHE no TLS 1.2 e obrigatório no TLS 1.3), possuir a chave privada RSA do certificado do servidor **não** permite mais decifrar capturas PCAP passivas; a decriptação forense moderna no Wireshark/TShark baseia-se em segredos de sessão efêmeros (**`SSLKEYLOGFILE`**) ou arquivos **`keytab` Kerberos**.

## Por que importa
Ao investigar um malware em sandbox, depurar um microsserviço ou capturar tráfego em um proxy reverso, exportar a variável `SSLKEYLOGFILE=/tmp/tls-secrets.log` faz bibliotecas como OpenSSL, BoringSSL, NSS (Firefox/Chrome) e GnuTLS gravarem os segredos `CLIENT_HANDSHAKE_TRAFFIC_SECRET` / `SERVER_TRAFFIC_SECRET_0` (formato NSS Key Log), que o `tshark` consome via **`-o tls.keylog_file:/tmp/tls-secrets.log`**.

## Como funciona
Mais ainda, o utilitário **`editcap --inject-secrets tls,/tmp/tls-secrets.log input.pcapng output_with_dsb.pcapng`** embute apenas os segredos necessários dentro de um bloco **DSB (*Decryption Secrets Block*)** do próprio arquivo `.pcapng`, permitindo compartilhar um único arquivo autocontido com outros peritos do CSIRT.

## Exemplo
```bash
# Embutir os segredos de sessao TLS 1.3 dentro do PCAPNG (bloco DSB) e inspecionar requisicoes HTTP/2 decifradas
editcap --inject-secrets tls,/cases/pcaps/sslkeylog.txt \
  /cases/pcaps/raw_capture.pcapng \
  /cases/pcaps/decrypted_ready.pcapng

tshark -r /cases/pcaps/decrypted_ready.pcapng -n -Y "http2.headers.path" \
  -T fields -e ip.src -e http2.headers.authority -e http2.headers.path
```

## Limites e trade-offs
Em investigações de Active Directory, passar `-o kerberos.decrypt:TRUE -o kerberos.file:/cases/krbtgt.keytab` ao `tshark` decifra tickets Kerberos AS-REQ/TGS-REQ/AP-REQ e sessões SMB/LDAP/RPC protegidas na captura.

## Como verificar
Confirme que o arquivo `.pcapng` gerado por `editcap --inject-secrets` exibe os quadros `http` / `http2` decifrados automaticamente ao ser aberto no Wireshark/TShark sem precisar configurar `tls.keylog_file` novamente.

## Conexões
- [[wireshark-estatisticas-forenses-tshark-z-conversations-io-follow]] — Veja também: `tshark`: Estatísticas Forenses (`-q -z conv,tcp`, `-z io,phs`, `-z endpoints`, `-z dns,tree`, `-z http,tree`) e Reconstrução de Streams (`-z follow`).
- [[wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark]] — Veja também: Wireshark & `tshark`: Extração Forense de Arquivos e Payloads Transferidos via Rede (`--export-objects http,smb,tftp,imf`).
- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Referência cruzada direta com wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.
- [[impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden]] — Referência cruzada direta com impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
