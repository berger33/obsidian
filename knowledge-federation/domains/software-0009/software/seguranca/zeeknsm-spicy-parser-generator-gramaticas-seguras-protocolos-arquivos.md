---
id: software.seguranca.tranche03.000208
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
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek `Spicy`: gerador moderno de parsers seguros em C++ para protocolos de rede e formatos de arquivo customizados

## Em uma frase
O Zeek integra nativamente o **Spicy** — uma linguagem declarativa e compilador de gramáticas que gera parsers C++ de alta performance e **seguros contra corrupção de memória** para novos protocolos de rede (TCP/UDP) e formatos de arquivo, substituindo a escrita manual de analisadores C++/BinPAC propensos a *buffer overflows*.

## Por que importa
Escrever um parser manual em C ou C++ para dissecar um protocolo binário complexo que chega diretamente da rede não confiável é uma das maiores fontes históricas de vulnerabilidades críticas (CVEs de leitura/escrita fora dos limites) em sensores de rede.

## Como funciona
No Spicy (arquivos `.spicy` e `.evt`), você declara a estrutura dos pacotes/mensagens como unidades tipadas (`public type Message = unit { ... }`) e o mapeamento direto para eventos do Zeek (`on MyProto::Message -> event myproto::message($conn, self.field);`); o compilador `spicyz` valida limites de bytes automaticamente e compila a gramática em código nativo carregável pelo Zeek!

## Exemplo
```bash
# Verificando o suporte embutido ao compilador Spicy na instalação do Zeek:
zeek --version
spicyc --version
```

## Limites e trade-offs
Muitos dos analisadores oficiais modernos do próprio Zeek (como QUIC, HTTP/3, OpenVPN, WireGuard, LDAP e DNS estendido) são implementados usando **Spicy**.

## Como verificar
Execute `zeek -NN | grep -i spicy` para listar todos os analisadores Spicy registrados no seu binário do Zeek.

## Conexões
- [[zeeknsm-arquitetura-cluster-zeekctl-manager-logger-proxy-workers]] — Veja também: Zeek Arquitetura de Cluster (`zeekctl` / `node.cfg`): papéis de `Manager`, `Logger`, `Proxy` e `Workers` com `AF_PACKET` e `lb_procs`.
- [[zeeknsm-package-manager-zkg-ja3-ja4-bzar-mitre-attack-extensoes]] — Veja também: Zeek Package Manager (`zkg`): instalação de pacotes comunitários (`JA3`, `JA4`, `MITRE ATT&CK BZAR`, `hassh`, `cve-detectors`).

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
