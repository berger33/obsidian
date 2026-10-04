---
id: software.seguranca.tranche04.000350
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md", "https://docs.projectdiscovery.io/opensource/subfinder/overview", "https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Subfinder: Monitoramento Contínuo de Novos Subdomínios, Detecção de *Shadow IT* e Subdomain Takeover

## Em uma frase
Executar o `subfinder` periodicamente via CronJob Kubernetes ou GitHub Actions e comparar o estado atual contra o inventário histórico permite alertar o SOC em minutos sempre que um novo subdomínio corporativo é criado ou recebe um certificado TLS.

## Por que importa
Novos subdomínios de campanha ou homologação frequentemente entram no ar com configurações padrão inseguras ou apontam via `CNAME` para serviços em nuvem desprovisionados (S3, Azure App Service, GitHub Pages), ficando vulneráveis a *Subdomain Takeover*.

## Como funciona
O job executa `subfinder -dL domains.txt -duc -silent`, ordena e deduplica a saída (`sort -u`), compara com a linha de base anterior (`comm -13 baseline.txt current.txt`) e submete apenas o delta de novos hosts para verificação de `CNAME` órfão e inspeção HTTP com `httpx`.

## Exemplo
```bash
# Detectar exclusivamente novos subdomínios surgidos desde a última varredura e sondá-los
subfinder -dL /etc/easm/domains.txt -duc -silent | sort -u > /tmp/current-subs.txt
comm -13 /var/lib/easm/baseline-subs.txt /tmp/current-subs.txt > /tmp/new-subs.txt

if [ -s /tmp/new-subs.txt ]; then
  httpx -l /tmp/new-subs.txt -silent -sc -cname -title -json -o /tmp/new-assets-alert.jsonl
  cp /tmp/current-subs.txt /var/lib/easm/baseline-subs.txt
fi
```

## Limites e trade-offs
Atualizar o arquivo `baseline-subs.txt` caso a execução do `subfinder` tenha falhado por falta de conectividade de rede fará com que na execução seguinte todos os subdomínios antigos pareçam novos; valide que `current-subs.txt` não está vazio antes de sobrescrever a base.

## Como verificar
Simule a adição de um domínio na base e verifique que `/tmp/new-subs.txt` isola apenas a diferença incremental (`comm -13`).

## Conexões
- [[subfinder-uso-como-biblioteca-go-sdk-runner-enumerate]] — Veja também: Subfinder: Integração Programática em Go via SDK (`runner.NewRunner` e `EnumerateSingleDomainWithCtx`).
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.
- [[subfinder-formatos-saida-jsonl-collect-sources-output-dir-audit]] — Referência cruzada direta com subfinder-formatos-saida-jsonl-collect-sources-output-dir-audit.
- [[httpxpd-probes-rede-ip-cname-asn-cdn-waf-vhost-ports]] — Referência cruzada direta com httpxpd-probes-rede-ip-cname-asn-cdn-waf-vhost-ports.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
