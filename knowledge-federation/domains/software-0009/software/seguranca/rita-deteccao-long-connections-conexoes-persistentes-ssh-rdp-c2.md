---
id: software.seguranca.tranche14.001364
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

# Caça a **Long Connections** (Conexões Persistentes) no RITA: Detectando Shells Reversos Interativos, Túneis SSH/Ngrok e Exfiltração Contínua

## Em uma frase
E se, em vez de usar um beacon periódico (*connect -> check-in -> disconnect*), o atacante abrir um **Shell Reverso Interativo persistente**, um túnel **SSH `-R` / Chisel / Ligolo-ng / Ngrok**, uma sessão **RDP** externa ou um stream contínuo de exfiltração que permanece conectado por horas?

## Por que importa
Como uma conexão única aberta durante 6 horas não gera múltiplos "intervalos entre conexões", ela não dispararia o detector de *Beaconing* periódico — mas é capturada imediatamente pelo detector de **`Long Connections`** do **RITA**!

## Como funciona
No arquivo `/etc/rita/config.hjson`, a seção **`scoring.long_connection`** pontua todas as conexões do `conn.log` do Zeek cuja duração acumulada (`duration`) ultrapassa os limiares configurados (`base: 3600` segundos = 1 hora, `low: 14400` = 4h, `medium: 28800` = 8h, `high: 43200` = 12h)!

## Exemplo
```hjson
// Configuracao de limiares de Long Connections (em segundos: 1h, 4h, 8h e 12h) no /etc/rita/config.hjson do RITA
scoring: {
  long_connection: {
    score_thresholds: {
      base: 3600
      low: 14400
      medium: 28800
      high: 43200
    }
  }
}
```

## Limites e trade-offs
Requisito crucial no sensor **Zeek** para que o detector de **Long Connections** do RITA enxergue conexões que ainda estão abertas (sem `FIN`/`RST`): por padrão, o Zeek só escreve uma linha no `conn.log` quando a conexão TCP termina! Por isso, ao usar o Zeek com o RITA, carregue o pacote oficial **`zeek-long-connections`** (ou o script de *heartbeats* de conexões ativas da Active Countermeasures) no Zeek para que conexões longas em andamento sejam registradas periodicamente no `conn.log`!

## Como verificar
No seu firewall de borda ou proxy corporativo, implemente também tempos máximos de sessão para impedir conexões HTTP/HTTPS que fiquem abertas por mais de algumas horas sem renegociação.

## Conexões
- [[rita-beaconing-sni-tls-domain-fronting-cdn-cloudflare-hunting]] — Veja também: Detecção de **SNI / FQDN Beaconing** no RITA: Caçando Implants C2 que Rotacionam IPs atrás de **CDNs (Cloudflare, CloudFront, Fastly, Azure Front Door)**.
- [[rita-deteccao-dns-tunneling-subdominios-unicos-iodine-dnscat2]] — Veja também: Detecção de **C2 e Exfiltração por DNS Tunneling (`iodine`, `dnscat2`, `sliver dns`, `cobalt strike dns`)** no RITA.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[rita-modificadores-score-prevalencia-raridade-first-seen-missing-host]] — Referência cruzada direta com rita-modificadores-score-prevalencia-raridade-first-seen-missing-host.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
