---
id: software.seguranca.tranche14.001363
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

# Detecção de **SNI / FQDN Beaconing** no RITA: Caçando Implants C2 que Rotacionam IPs atrás de **CDNs (Cloudflare, CloudFront, Fastly, Azure Front Door)**

## Em uma frase
O que acontece se o servidor C2 do atacante estiver escondido atrás de uma grande **CDN (como Cloudflare, AWS CloudFront ou Fastly)** ou usar DNS *Fast-Flux*, onde a cada conexão HTTPS do malware o nome de domínio (`c2-oculto.exemplo.com`) resolve para um **endereço IP de borda diferente** (`104.21.x.1`, depois `172.67.x.2`, depois `104.21.x.3`)?

## Por que importa
Se uma ferramenta de caça agrupar as conexões apenas pelo par `{IP_Interno -> IP_Externo}`, o beacon será dividido entre 10 IPs diferentes da CDN e parecerá irregular!

## Como funciona
É por isso que o **RITA** analisa os logs **`ssl.log`** e **`http.log`** do Zeek para calcular o **SNI / FQDN Beaconing**! Em vez de agrupar pelo IP de destino, o RITA agrupa todas as conexões de um host interno pelo **campo `server_name` (`SNI` do handshake TLS no `ssl.log`) ou cabeçalho `host` (`http.log`)**: mesmo que a conexão bata em 50 IPs diferentes da Cloudflare ao longo do dia, o RITA consolida todas as conexões para aquele `SNI` e revela o **score de Beaconing de 98% para o domínio do C2**!

## Exemplo
```bash
# Inspecionar nos logs do Zeek (ssl.log e conn.log) todas as conexoes de um host interno para um SNI suspeito sinalizado pelo RITA
zeek-cut ts uid id.orig_h id.resp_h server_name version cipher < /nsm/zeek/logs/current/ssl.log \
  | awk '$3 == "10.1.2.15" && $5 == "api-sync-telemetry.exemplo.org"'
```

## Limites e trade-offs
Quando o RITA aponta um score alto de Beaconing para um **SNI / FQDN**, qual é o próximo passo imediato do caçador de ameaças? Rodar a consulta `zeek-cut` acima no `ssl.log` e no `dns.log` para verificar: **(1) Quantos hosts da sua empresa acessam aquele domínio?** (se apenas `1` máquina de `2.000` acessa `api-sync-telemetry.exemplo.org` a cada 5 minutos durante a madrugada, a chance de ser C2 é altíssima!); **(2) Qual é a idade do domínio no Whois (`Cont3xt`)?**; e **(3) Qual é o fingerprint `JA3`/`JA4` do cliente TLS**!

## Como verificar
Combine sempre a análise de SNI do RITA com a inspeção do certificado e do `JA3`/`JA4` no **Arkime** e no **Zeek**.

## Conexões
- [[rita-matematica-deteccao-beacons-intervalos-jitter-tamanho-score]] — Veja também: A Matemática da Detecção de **Beaconing C2 (Com e Sem *Jitter*)** no RITA: Desvio de Intervalos (`Delta Times`), Simetria de Bytes, dispersão MADM e Score.
- [[rita-deteccao-long-connections-conexoes-persistentes-ssh-rdp-c2]] — Veja também: Caça a **Long Connections** (Conexões Persistentes) no RITA: Detectando Shells Reversos Interativos, Túneis SSH/Ngrok e Exfiltração Contínua.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting]] — Referência cruzada direta com arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
