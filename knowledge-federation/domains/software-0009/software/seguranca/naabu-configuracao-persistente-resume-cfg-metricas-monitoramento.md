---
id: software.seguranca.tranche09.000819
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod", "https://docs.projectdiscovery.io/tools/naabu/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Naabu: Arquivo de Configuração Persistente (`~/.config/naabu/config.yaml`), Retomada de Varredura (**`-resume`**) e Telemetria (`-metrics-port`)

## Em uma frase
Em varreduras de longa duração sobre milhares de ativos, se o processo do Naabu for interrompido com `Ctrl+C`, ele grava automaticamente o progresso no arquivo **`resume.cfg`**, permitindo retomar de onde parou passando a flag **`-resume`**!

## Por que importa
Para padronizar resolvers DNS customizados (`-r`), limites de taxa (`rate`), threads (`c`), retries e exclusões sem repetir flags na CLI, o Naabu lê automaticamente o arquivo YAML em **`~/.config/naabu/config.yaml`** (ou o caminho indicado por `-config`).

## Como funciona
E quando executado como um worker contínuo em uma plataforma interna de EASM, a flag **`-stats`** (ou o endpoint HTTP exposto por **`-mp` / `-metrics-port 63636`**) fornece telemetria em tempo real do percentual concluído, pacotes enviados por segundo e portas descobertas.

## Exemplo
```yaml
# ~/.config/naabu/config.yaml — Configuracao padrao endurecida para execucoes corporativas do Naabu
rate: 1000
c: 25
retries: 2
timeout: 1000
exclude-cdn: true
exclude-ports: 9100
resolvers:
  - 1.1.1.1
  - 8.8.8.8
  - 9.9.9.9
```

## Limites e trade-offs
Use **`naabu -hc` (`-health-check`)** para diagnosticar permissões de raw sockets (`CAP_NET_RAW` / `libpcap`), conectividade de rede, limites de descritores de arquivo (`fdmax`) e configuração do sistema operacional antes de rodar uma varredura grande.

## Como verificar
Execute `naabu -hc` na estação de segurança e verifique que todos os checks de rede e permissões reportam `OK`.

## Conexões
- [[naabu-entrada-asn-cidr-exclusao-escopo-exclude-hosts-file]] — Veja também: Naabu: Varredura Direta por **ASN (`AS1449`) e CIDR**, Exclusão de Escopo (`-eh` / `-ef`) e Política de Rede (`networkpolicy`).
- [[naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei]] — Veja também: Pipeline Unix ProjectDiscovery Completo: **`subfinder` -> `dnsx` -> `naabu` -> `httpx` -> `katana` -> `nuclei`**.
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo]] — Referência cruzada direta com masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo.
- [[rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis]] — Referência cruzada direta com rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
