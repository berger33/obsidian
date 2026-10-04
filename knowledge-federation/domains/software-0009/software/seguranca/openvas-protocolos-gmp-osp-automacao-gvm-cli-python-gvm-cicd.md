---
id: software.seguranca.tranche16.001506
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

# Automação do Greenbone com **`gvm-cli`**, **`python-gvm`** e Protocolo **GMP (`Greenbone Management Protocol`)** sobre Unix Socket / TLS

## Em uma frase
Como automatizar 100% da operação do Greenbone/OpenVAS — criar Targets a partir do inventário da nuvem, disparar Tasks de varredura após um deploy, acompanhar a porcentagem de progresso e baixar relatórios em **XML, JSON, PDF ou CSV** — via linha de comando ou scripts Python?

## Por que importa
Através da suíte oficial **`gvm-tools` (`gvm-cli`, `gvm-script`, `gvm-pyshell`)** e da biblioteca **`python-gvm`**, que conversam diretamente com o `gvmd` usando o protocolo XML **`GMP` (*Greenbone Management Protocol*)** sobre o socket Unix `/run/gvmd/gvmd.sock` (ou SSH/TLS)!

## Como funciona
Além da autenticação tradicional com usuário/senha, o `README.md` do `gvmd` documenta o suporte nativo a **Autenticação via Tokens JWT (`[authentication]` em `gvmd.conf`)**: configurando `jwt_secret_type` (`ECDSA`, `RSA` ou `shared`), `jwt_encode_secret_path`, `jwt_decode_secret_path` e `jwt_access_duration` (padrão `60` segundos)!

## Exemplo
```bash
# Consultar via gvm-cli (sobre o Unix socket do gvmd) a versao do protocolo GMP e listar todas as Tasks de varredura e seus status
gvm-cli --gmp-username admin --gmp-password "${GVM_PASS}" \
  socket --socketpath /run/gvmd/gvmd.sock \
  --xml "<get_tasks/>"
```

## Limites e trade-offs
Para automações complexas em Python (como cruzar os resultados do OpenVAS com tickets do Jira ou enviar para o **OWASP DefectDojo**), em vez de concatenar strings XML na mão, use a API Pythonica do **`python-gvm`** (`with UnixSocketConnection(path="/run/gvmd/gvmd.sock") as connection: with Gmp(connection=connection) as gmp: gmp.get_tasks()`)!

## Como verificar
E como o `README.md` do `gvmd` documenta na seção *Security Intelligence export*, o `gvmd` também possui retentativa exponencial configurável (`max_retries=10`, `retry_base_delay=10`, `retry_multiplier=2`, `retry_max_delay=600`, `stale_threshold=720`) para exportação automática de relatórios para plataformas de inteligência de segurança.

## Conexões
- [[openvas-perfis-varredura-full-and-fast-cve-scan-matching-version]] — Veja também: Perfis de Varredura (**`Full and fast`**, **`Host Discovery`**, **`System Discovery`**) e o **`CVE Scan` (`cve_scan_matching_version`)** no `gvmd`.
- [[openvas-linguagem-nasl-scripts-nvt-openvas-nasl-execucao-isolada]] — Veja também: Anatomia dos Testes de Vulnerabilidade **NASL (*Network Attack Scripting Language*)** e Execução Isolada de Debug com **`openvas-nasl`**.
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Referência cruzada direta com openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa.
- [[openvas-gestao-resultados-qod-quality-of-detection-overrides-false-positives]] — Referência cruzada direta com openvas-gestao-resultados-qod-quality-of-detection-overrides-false-positives.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
