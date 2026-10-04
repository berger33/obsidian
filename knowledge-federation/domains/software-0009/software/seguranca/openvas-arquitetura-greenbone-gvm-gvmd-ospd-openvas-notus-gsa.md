---
id: software.seguranca.tranche16.001501
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md", "https://raw.githubusercontent.com/greenbone/gvmd/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **Greenbone Vulnerability Management (GVM / OpenVAS)**: **`gvmd` (`GMP`)**, **`ospd-openvas` (`OSP`)**, **`openvas-scanner`**, **`notus-scanner`** e PostgreSQL/Redis

## Em uma frase
Como a plataforma open-source de gerenciamento de vulnerabilidades mais completa do mundo — o **Greenbone Vulnerability Management (`GVM`, sucessor moderno do `OpenVAS`)** — divide responsabilidades entre gerenciamento, varredura ativa de rede e verificação local de pacotes?

## Por que importa
Conforme documentado nos repositórios oficiais `greenbone/openvas-scanner` e `greenbone/gvmd`, a pilha GVM moderna é modular e orientada a dois protocolos XML/JSON bem definidos: **(1) `gvmd` (*Greenbone Vulnerability Manager*)** é o cérebro central que armazena configurações, agendamentos, ativos e relatórios no **PostgreSQL** (com a extensão `pg-gvm`) e expõe o **GMP (*Greenbone Management Protocol*)** para a interface web **GSA (`gsad`)** e para o CLI **`gvm-cli`**.

## Como funciona
**(2) `ospd-openvas` + `openvas-scanner` (e a nova implementação unificada em Rust `openvasd`)**: recebem ordens de varredura do `gvmd` via **OSP (*Open Scanner Protocol*)**, executam os testes **NASL (*Network Attack Scripting Language*)** usando o **Redis** como Knowledge Base (`KB`) em memória de alta velocidade e trabalham em conjunto com o **`notus-scanner`** (verificador rápido de pacotes locais via MQTT)!

## Exemplo
```bash
# Inspecionar o status dos servicos e containers oficiais da pilha Greenbone Community Edition (gvmd, ospd-openvas, notus-scanner, redis e pg-gvm)
gvmd --version
openvas -V
gvm-cli --version
```

## Limites e trade-offs
Por que o `openvas-scanner` utiliza uma instância dedicada do **Redis sobre Unix Domain Socket (`/run/redis-openvas/redis.sock`)** durante cada varredura? Porque uma única varredura executa dezenas de milhares de scripts **NASL** dependentes entre si: quando o script de descoberta de versão do OpenSSH ou HTTP salva um banner na **Knowledge Base (`KB`)** no Redis, todos os scripts NASL seguintes leem essa informação da RAM em microssegundos sem precisar reconectar ao host alvo!

## Como verificar
Como destaca o `README.md` do `openvas-scanner`, todos os pacotes e artefatos do **Greenbone Community Feed** são assinados criptograficamente com a chave GPG oficial `8AE4 BE42 9B60 A59B 311C 2E73 9823 FAA6 0ED1 E580`.

## Conexões
- [[openvas-sincronizacao-feeds-greenbone-nvt-scap-cert-gvmd-data]] — Veja também: Sincronização dos Feeds de Inteligência do Greenbone (**`greenbone-feed-sync`**): **NVTs (NASL)**, **SCAP (`CVE` / `CPE`)**, **CERT (`DFN-CERT`)** e **`GVMD_DATA`**.
- [[openvas-protocolos-gmp-osp-automacao-gvm-cli-python-gvm-cicd]] — Referência cruzada direta com openvas-protocolos-gmp-osp-automacao-gvm-cli-python-gvm-cicd.
- [[openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds]] — Referência cruzada direta com openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
