---
id: software.seguranca.tranche03.000201
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek Network Security Monitor: arquitetura em duas camadas (*Event Engine* e *Script Interpreter*) para análise semântica de rede

## Em uma frase
Conforme documentado na seção oficial *Architecture* (`doc/about/architecture.rst`) e no README do repositório, o **Zeek** (`zeek/zeek`, anteriormente conhecido como *Bro*, licenciado sob BSD-3-Clause) é um framework poderoso de análise de tráfego e **Network Security Monitoring (NSM)** estruturado em duas camadas fundamentais: o **Event Engine (Core)** e o **Script Interpreter**.

## Por que importa
Ao contrário de um IDS tradicional baseado apenas em casar assinaturas estáticas de bytes para emitir alertas pontuais, o Zeek reconstrói o estado completo da camada de aplicação e produz um arquivo histórico rico e semântico de toda a atividade da rede.

## Como funciona
O **Event Engine** consome pacotes da interface de rede (ou PCAP), realiza análise de pacotes, análise de sessão (HTTP, DNS, TLS/SSL, SMB, Kerberos, SSH, RDP, FTP, SMTP) e análise de arquivos, reduzindo o fluxo de pacotes em **eventos neutros de política** (como `connection_established`, `http_request`, `dns_request`). Em seguida, o **Script Interpreter** executa programas na linguagem de domínio específico do Zeek (*Zeek Scripting Language*) que correlacionam eventos ao longo do tempo, geram todos os logs padrão e aplicam as políticas de detecção do site!

## Exemplo
```bash
# Analisando um arquivo PCAP com o Zeek e gerando os logs transacionais estruturados no diretório atual:
zeek -C -r captura-rede.pcap local
ls -la *.log
```

## Limites e trade-offs
Use sempre a flag **`-C`** (`--no-checksums`) ao processar arquivos `.pcap` capturados em interfaces com *TCP Checksum Offloading*, evitando que o Event Engine ignore segmentos TCP com checksum ainda não calculado pela placa de rede.

## Como verificar
Execute `zeek --version` e processe um PCAP de teste verificando a geração de `conn.log`, `dns.log`, `http.log` e `ssl.log`.

## Conexões
- [[zeeknsm-logs-transacionais-conn-dns-http-ssl-files-x509-uid]] — Veja também: Zeek Logs Transacionais e Correlação por `uid` (`conn.log`, `dns.log`, `http.log`, `ssl.log`, `files.log`): pivotamento forense no SOC.

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
