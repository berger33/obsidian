---
id: software.seguranca.tranche09.000820
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

# Pipeline Unix ProjectDiscovery Completo: **`subfinder` -> `dnsx` -> `naabu` -> `httpx` -> `katana` -> `nuclei`**

## Em uma frase
O verdadeiro poder do **Naabu** aparece quando ele ocupa o elo central do pipeline modular da ProjectDiscovery: sem o Naabu entre o `subfinder`/`dnsx` e o `httpx`, o `httpx` testaria por padrão apenas as portas web padrão (`80` e `443`), deixando passar aplicações administrativas críticas rodando nas portas **`8080`, `8443`, `8888`, `9000`, `9090`, `3000`, `5000`, `7001` (WebLogic) ou `4848` (GlassFish)**!

## Por que importa
Inserir **`| naabu -silent -top-ports 1000 -exclude-cdn |`** antes do `httpx` descobre todas as portas TCP abertas em cada subdomínio vivo (poupando tempo em CDNs com `-exclude-cdn`) e entrega pares `subdominio.exemplo.com.br:8443` na entrada padrão do `httpx`!

## Como funciona
O `httpx` então sonda todas essas portas não-padrão em busca de servidores HTTP/HTTPS ativos, que por sua vez alimentam o `katana` (crawling) e o `nuclei` (detecção de CVEs e misconfigurations)!

## Exemplo
```bash
# Pipeline completo de descoberta de superficie web em portas padrao e nao-padrao (Subfinder -> dnsx -> Naabu -> httpx -> Nuclei)
subfinder -d exemplo.com.br -silent \
  | dnsx -silent \
  | naabu -silent -top-ports 1000 -exclude-cdn -rate 1500 \
  | httpx -silent \
  | nuclei -t http/exposures/ -t http/misconfiguration/ -o /cases/easm/full_pipeline_findings.txt
```

## Limites e trade-offs
Quando encadear ferramentas em tempo real onde o fluxo de entrada é contínuo, você pode usar a flag **`-stream`** no Naabu para que ele processe e emita cada host imediatamente à medida que chega no `stdin`.

## Como verificar
Compare a quantidade de serviços web encontrados por `subfinder | httpx` (apenas 80/443) vs `subfinder | naabu -top-ports 1000 -ec | httpx` (todas as portas web altas!).

## Conexões
- [[naabu-configuracao-persistente-resume-cfg-metricas-monitoramento]] — Veja também: Naabu: Arquivo de Configuração Persistente (`~/.config/naabu/config.yaml`), Retomada de Varredura (**`-resume`**) e Telemetria (`-metrics-port`).
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
