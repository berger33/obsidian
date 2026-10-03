---
id: software.seguranca.tranche06.000556
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

# Wireshark & `tshark`: Extração Forense de Arquivos e Payloads Transferidos via Rede (`--export-objects http,smb,tftp,imf`)

## Em uma frase
A opção **`--export-objects <protocol>,<destdir>`** do `tshark` (equivalente a *File -> Export Objects* no Wireshark) remonta automaticamente fluxos TCP e extrai para o disco todos os arquivos transferidos sobre **HTTP**, **SMB/SMB2**, **IMF** (e-mails SMTP/MIME), **TFTP** e **DICOM**.

## Por que importa
Quando um host comprometido baixa um estágio secundário via HTTP (`GET /update.dll`) ou quando um atacante copia ferramentas lateralmente por compartilhamentos administrativos Windows (`\\HOST\ADMIN$\svc.exe` via SMB2), o `--export-objects` reconstrói o binário exato a partir do PCAP para cálculo de SHA-256 e submissão ao YARA/CAPEv2.

## Como funciona
Para transferências SMB2/SMB3, desde que o tráfego SMB não esteja cifrado com *SMB Encryption* (ou que a chave de sessão seja conhecida), o dissecador SMB2 remonta leituras e escritas parciais (`SMB2 READ` / `SMB2 WRITE`) identificando o nome do arquivo no `Tree Connect` / `Create`.

## Exemplo
```bash
# Extrair todos os binarios e scripts transferidos via HTTP e SMB2 de um PCAP de incidente e calcular hashes
mkdir -p /tmp/extracted-http /tmp/extracted-smb
tshark -r /cases/pcaps/incident.pcapng -n -q \
  --export-objects http,/tmp/extracted-http \
  --export-objects smb,/tmp/extracted-smb

sha256sum /tmp/extracted-http/* /tmp/extracted-smb/* 2>/dev/null
```

## Limites e trade-offs
Sempre execute a extração de objetos em um diretório isolado em sistema de arquivos montado com `noexec` na máquina de análise forense para impedir execução acidental de malwares extraídos do PCAP.

## Como verificar
Verifique os arquivos extraídos em `/tmp/extracted-http` e `/tmp/extracted-smb` com `file` e `yara` para confirmar a integridade da reconstrução.

## Conexões
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Veja também: Wireshark & `tshark`: Decriptação Passiva de Tráfego **TLS 1.2/1.3** (`SSLKEYLOGFILE` e `editcap --inject-secrets`) e **Kerberos** (`keytab`).
- [[wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc]] — Veja também: Wireshark & `tshark`: Filtros de Detecção de Ataques em Active Directory (Kerberos Roasting, `DCSync` `DRSUAPI`, NTLM Relay e `psexec`).
- [[wireshark-estatisticas-forenses-tshark-z-conversations-io-follow]] — Referência cruzada direta com wireshark-estatisticas-forenses-tshark-z-conversations-io-follow.
- [[capev2-integracao-api-rest-v2-automacao-submissao-thehive-misp]] — Referência cruzada direta com capev2-integracao-api-rest-v2-automacao-submissao-thehive-misp.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
