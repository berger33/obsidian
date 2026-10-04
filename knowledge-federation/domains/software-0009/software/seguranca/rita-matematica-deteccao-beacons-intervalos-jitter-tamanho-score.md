---
id: software.seguranca.tranche14.001362
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

# A Matemática da Detecção de **Beaconing C2 (Com e Sem *Jitter*)** no RITA: Desvio de Intervalos (`Delta Times`), Simetria de Bytes, dispersão MADM e Score

## Em uma frase
Quando um operador de Red Team ou atacante configura um beacon C2 com **`Jitter` (variação aleatória no tempo de espera, ex.: `sleep 60` segundos com `30% jitter`)**, ele espera enganar detectores ingênuos que procuram apenas intervalos perfeitamente idênticos. Como o algoritmo estatístico de **Beaconing do RITA** derrota o *Jitter* e pontua cada par `{Host Interno -> Destino Externo}` de `0` a `100%`?

## Por que importa
O RITA analisa **duas dimensões independentes** de todas as conexões entre o host de origem e o destino ao longo do período importado: **(1) Consistência dos Intervalos de Tempo (`Time Deltas`: `t_1 - t_0`, `t_2 - t_1`, ...)** e **(2) Consistência do Tamanho dos Dados Enviados/Recebidos (`Data Size Distribution` em `orig_ip_bytes`)**!

## Como funciona
Em cada dimensão, em vez de usar média e desvio-padrão simples (que são facilmente distorcidos por poucos *outliers* ou *jitter*), o RITA utiliza estatísticas robustas de ordem: **Quartis (Bowley Skewness — assimetria da distribuição entre `Q1`, `Mediana Q2` e `Q3`)** e **MADM (*Median Absolute Deviation about the Median* — dispersão em torno da mediana)**! Um beacon com *jitter* uniforme de 30% em torno de 60s continua tendo uma distribuição perfeitamente **simétrica (`Skewness ~ 0`)** em torno da mediana de 60s e tamanhos de pacotes de *heartbeat* (`check-in` vazio) quase constantes!

## Exemplo
```hjson
// Secao de calibracao de thresholds de Beaconing no arquivo /etc/rita/config.hjson do RITA
scoring: {
  beacon: {
    unique_connection_threshold: 4
    score_thresholds: {
      base: 50
      low: 75
      medium: 90
      high: 100
    }
  }
}
```

## Limites e trade-offs
Veja na configuração `/etc/rita/config.hjson` acima: o `unique_connection_threshold: 4` define o número mínimo de conexões necessárias para calcular o score estatístico de beacon, e os `score_thresholds` classificam a severidade final (`base: 50`, `low: 75`, `medium: 90`, `high: 100`) combinando o score de periodicidade temporal, o score de tamanho de payload e os modificadores de contexto!

## Como verificar
E quando um implante faz conexões tão frequentes (ex.: a cada 1 segundo, gerando mais de 86.400 conexões por dia) que parece um fluxo quase contínuo? O RITA classifica esse padrão separadamente como **`Strobe`** e aplica automaticamente a pontuação **`strobe_impact: { category: "high" }`**!

## Conexões
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Veja também: Arquitetura do **RITA (`activecm/rita` — *Real Intelligence Threat Analytics*)**: Caça a Ameaças (**Threat Hunting**) em Logs **Zeek** para Detecção de **C2 Beaconing**.
- [[rita-beaconing-sni-tls-domain-fronting-cdn-cloudflare-hunting]] — Veja também: Detecção de **SNI / FQDN Beaconing** no RITA: Caçando Implants C2 que Rotacionam IPs atrás de **CDNs (Cloudflare, CloudFront, Fastly, Azure Front Door)**.
- [[rita-modificadores-score-prevalencia-raridade-first-seen-missing-host]] — Referência cruzada direta com rita-modificadores-score-prevalencia-raridade-first-seen-missing-host.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
