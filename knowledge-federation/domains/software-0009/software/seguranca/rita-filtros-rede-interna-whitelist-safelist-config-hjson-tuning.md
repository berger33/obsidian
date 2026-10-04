---
id: software.seguranca.tranche14.001367
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/activecm/rita/main/README.md", "https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Configuração de Sub-redes Internas (**`internal_subnets`**) e Listas de Exclusão (**`never_included_ips` / `never_included_domains`**) no `/etc/rita/config.hjson`

## Em uma frase
Por que a configuração correta da lista **`filter.internal_subnets`** no `/etc/rita/config.hjson` é a primeira coisa que você deve conferir antes de rodar o `rita import` em qualquer ambiente corporativo ou de nuvem?

## Por que importa
Porque o RITA determina a direção dos fluxos (`Interno -> Externo`, `Interno -> Interno`) com base em `internal_subnets`! Por padrão, ele inclui as faixas privadas **`RFC 1918` (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`)**, mas se a sua empresa utilizar um bloco de IPs públicos próprios roteados internamente, sub-redes Carrier-Grade NAT (`100.64.0.0/10` usadas por Tailscale/NetBird!) ou IPv6 interno, você deve adicioná-los em `internal_subnets`!

## Como funciona
Além disso, o bloco `filter` do `config.hjson` permite manter uma **Safelist cirúrgica (`never_included_ips`, `never_included_domains` com suporte a curinga `*.dominio.com`)** para remover do cálculo analítico servidores de atualização ou parceiros já auditados e reduzir o ruído no SOC!

## Exemplo
```hjson
// Configuracao da secao filter no /etc/rita/config.hjson com sub-redes internas (RFC 1918 + CGNAT VPN) e dominios confiaveis excluidos
filter: {
  internal_subnets: [
    "10.0.0.0/8",
    "172.16.0.0/12",
    "192.168.0.0/16",
    "100.64.0.0/10"
  ]
  never_included_ips: [
    "8.8.8.8/32",
    "1.1.1.1/32"
  ]
  never_included_domains: [
    "*.windowsupdate.com",
    "*.zen.spamhaus.org"
  ]
  filter_external_to_internal: true
}
```

## Limites e trade-offs
Cuidado extremo ao adicionar domínios com curinga (`*.dominio.com`) em **`never_included_domains`**: **JAMAIS coloque na safelist domínios de nuvens compartilhadas ou CDNs onde qualquer atacante pode hospedar um worker ou bucket (como `*.amazonaws.com`, `*.cloudfront.net`, `*.workers.dev`, `*.azurewebsites.net`, `*.github.io` ou `*.ngrok-free.app`)**! Se você colocar uma CDN pública na safelist, ficará cego para qualquer C2 que use *Domain Fronting* ou *Cloud Redirectors* naquela nuvem!

## Como verificar
Para testar um arquivo de configuração customizado sem alterar o `/etc/rita/config.hjson` global, passe a flag **`-c ./meu_config.hjson`** no comando `rita`.

## Conexões
- [[rita-modificadores-score-prevalencia-raridade-first-seen-missing-host]] — Veja também: Modificadores Inteligentes de Score (**`modifiers`**) no RITA: **Prevalência na Rede (`prevalence`)**, **`first_seen`** e **`missing_host_count` (Conexões Diretas a IP Sem DNS)**.
- [[rita-threat-intel-feeds-customizados-online-ip-fqdn-correlacao]] — Veja também: Integração de Feeds de **Threat Intelligence (`threat_intel`)** no RITA: Cruzando Conexões Zeek com Listas de IoCs (`online_feeds` e Feeds Customizados).
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[rita-beaconing-sni-tls-domain-fronting-cdn-cloudflare-hunting]] — Referência cruzada direta com rita-beaconing-sni-tls-domain-fronting-cdn-cloudflare-hunting.
- [[rita-deteccao-dns-tunneling-subdominios-unicos-iodine-dnscat2]] — Referência cruzada direta com rita-deteccao-dns-tunneling-subdominios-unicos-iodine-dnscat2.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
