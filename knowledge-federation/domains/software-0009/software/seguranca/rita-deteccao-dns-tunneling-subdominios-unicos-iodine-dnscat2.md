---
id: software.seguranca.tranche14.001365
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

# Detecção de **C2 e Exfiltração por DNS Tunneling (`iodine`, `dnscat2`, `sliver dns`, `cobalt strike dns`)** no RITA

## Em uma frase
Por que tantos grupos de APT e *ransomware* usam **DNS Tunneling** como canal de Comando e Controle de fallback ou para exfiltrar dados de redes altamente restritas? Porque mesmo em segmentos de rede onde o firewall bloqueia 100% do acesso direto à Internet (portas 80/443 fechadas), os servidores internos quase sempre têm permissão para enviar consultas DNS (`UDP :53`) ao resolvedor DNS interno — que recursivamente encaminha a consulta para o servidor DNS autoritativo controlado pelo atacante (`*.c2-atacante.com`)!

## Por que importa
Como funciona um túnel DNS (`dnscat2`, `iodine`, `dns2tcp`) e por que toda requisição precisa ser diferente? Para enviar dados para fora e impedir que o resolvedor DNS intermediário devolva uma resposta do cache em vez de falar com o servidor do atacante, o malware codifica os bytes em **centenas ou milhares de subdomínios únicos nunca vistos antes** (ex.: `a8f9b2c104.dados.c2-atacante.com`, `77e1d4a902.dados.c2-atacante.com`)!

## Como funciona
O módulo de **DNS Tunneling / C2 over DNS** do **RITA** analisa o `dns.log` do Zeek contando exatamente o **número de subdomínios únicos consultados sob cada domínio raiz (`eTLD+1`)**!

## Exemplo
```hjson
// Configuracao de deteccao de C2/Exfiltracao via DNS (contagem de subdominios unicos para um mesmo dominio raiz) no /etc/rita/config.hjson
scoring: {
  c2: {
    score_thresholds: {
      base: 100
      low: 250
      medium: 500
      high: 1000
    }
  }
}
```

## Limites e trade-offs
Repare na simplicidade e letalidade estatística dessa métrica no RITA (`scoring.c2.score_thresholds`: `base: 100`, `low: 250`, `medium: 500`, `high: 1000` subdomínios únicos): um site normal tem meia dúzia de subdomínios (`www`, `mail`, `api`, `cdn`); já qualquer ferramenta de **DNS Tunneling ou exfiltração via DNS** precisa gerar centenas ou milhares de subdomínios únicos para transmitir meros kilobytes de dados, estourando imediatamente o score `high: 1000` no RITA!

## Como verificar
Atenção aos únicos falsos positivos legítimos conhecidos de *subdomínios únicos em massa* em redes corporativas: servidores de e-mail consultando listas anti-spam **DNSBL (`*.zen.spamhaus.org`)** e alguns antivírus legados que consultam hashes via DNS (`*.avts.mcafee.com`) — basta adicioná-los na lista `filter.never_included_domains` do `/etc/rita/config.hjson`!

## Conexões
- [[rita-deteccao-long-connections-conexoes-persistentes-ssh-rdp-c2]] — Veja também: Caça a **Long Connections** (Conexões Persistentes) no RITA: Detectando Shells Reversos Interativos, Túneis SSH/Ngrok e Exfiltração Contínua.
- [[rita-modificadores-score-prevalencia-raridade-first-seen-missing-host]] — Veja também: Modificadores Inteligentes de Score (**`modifiers`**) no RITA: **Prevalência na Rede (`prevalence`)**, **`first_seen`** e **`missing_host_count` (Conexões Diretas a IP Sem DNS)**.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[rita-filtros-rede-interna-whitelist-safelist-config-hjson-tuning]] — Referência cruzada direta com rita-filtros-rede-interna-whitelist-safelist-config-hjson-tuning.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
