---
id: software.seguranca.tranche16.001507
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

# Anatomia dos Testes de Vulnerabilidade **NASL (*Network Attack Scripting Language*)** e Execução Isolada de Debug com **`openvas-nasl`**

## Em uma frase
Quando o relatório do OpenVAS aponta uma vulnerabilidade específica (identificada por um **`OID`**, ex.: `1.3.6.1.4.1.25623.1.0.108560`) e o time de desenvolvimento pergunta *"O que exatamente o scanner testou para chegar a essa conclusão?"*, como inspecionar o código-fonte do teste e reexecutá-lo isoladamente em 2 segundos sem rodar um scan inteiro?

## Por que importa
Todos os testes da Greenbone Community Edition são arquivos de texto abertos escritos na linguagem **`NASL` (*Network Attack Scripting Language*)**, armazenados localmente em **`/var/lib/openvas/plugins/`**!

## Como funciona
E o binário `openvas-scanner` vem acompanhado do interpretador de linha de comando **`openvas-nasl`** (e `openvas-nasl-lint`), que permite executar **um único script `.nasl` diretamente contra um IP de teste** no terminal com debug detalhado (`-X -B -d -i /var/lib/openvas/plugins -t 192.0.2.10 script.nasl`)!

## Exemplo
```bash
# Localizar o script .nasl pelo seu OID, validar sua sintaxe e executa-lo isoladamente contra um host de laboratorio com openvas-nasl
grep -rn "1.3.6.1.4.1.25623.1.0.10330" /var/lib/openvas/plugins/ | head -n 5
openvas-nasl -X -B -i /var/lib/openvas/plugins -t 192.0.2.10 httpver.nasl
```

## Limites e trade-offs
Veja o significado das flags do **`openvas-nasl`** acima: **`-i /var/lib/openvas/plugins`** aponta o diretório de `.inc` (*includes* NASL compartilhados como `http_func.inc`, `ssh_func.inc`, `host_details.inc`); **`-t <IP>`** define o alvo; **`-B`** executa a seção `description` para carregar metadados; e **`-X`** roda o script em modo autenticado/não-assinado para testes locais e desenvolvimento de novos NVTs!

## Como verificar
Inspecionar o código `.nasl` em `/var/lib/openvas/plugins/` é a forma mais rápida e transparente de comprovar a evidência técnica exata de qualquer achado do OpenVAS.

## Conexões
- [[openvas-protocolos-gmp-osp-automacao-gvm-cli-python-gvm-cicd]] — Veja também: Automação do Greenbone com **`gvm-cli`**, **`python-gvm`** e Protocolo **GMP (`Greenbone Management Protocol`)** sobre Unix Socket / TLS.
- [[openvas-gestao-resultados-qod-quality-of-detection-overrides-false-positives]] — Veja também: Triagem de Resultados no Greenbone: **QoD (*Quality of Detection* — `70%` Default)**, **Notes**, **Overrides** e Filtragem de Falsos Positivos.
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Referência cruzada direta com openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
