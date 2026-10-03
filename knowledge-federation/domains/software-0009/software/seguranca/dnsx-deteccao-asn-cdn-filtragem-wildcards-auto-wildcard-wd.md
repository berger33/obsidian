---
id: software.seguranca.tranche09.000822
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod", "https://docs.projectdiscovery.io/tools/dnsx/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `dnsx`: Filtragem Automática de **DNS Wildcards (`-wd` / `-auto-wildcard`, `-wt`)** e Enriquecimento de **ASN (`-asn`) e CDN (`-cdn`)**

## Em uma frase
Domínios corporativos frequentemente possuem registros **DNS Wildcard (`*.dev.exemplo.com.br -> 198.51.100.10`)**: durante uma enumeração por wordlist, qualquer palavra inexistente (`qualquercoisa123.dev.exemplo.com.br`) retorna `NOERROR` com o IP `198.51.100.10`, gerando 100.000 falsos positivos se o resolvedor não filtrar wildcards!

## Por que importa
O `dnsx` implementa filtragem inteligente de Wildcard em múltiplos níveis (inspirada no `shuffledns`) através das flags **`-wd <dominio>` (`-wildcard-domain`)**, **`-auto-wildcard`** e **`-wt <limiar>` (`-wildcard-threshold`, padrão `5`)**: quando mais de `N` subdomínios na mesma sub-árvore apontam para o mesmo conjunto de IPs, o `dnsx` sonda aquele nível com subdomínios aleatórios e **remove automaticamente todos os falsos positivos gerados pelo wildcard**!

## Como funciona
Ao mesmo tempo, passar as flags **`-asn`** e **`-cdn`** enriquece cada resposta DNS com o número/nome do Sistema Autônomo (`[AS13335 Cloudflare]`) e o provedor de CDN (`[cloudflare]`, `[cloudfront]`).

## Exemplo
```bash
# Resolver subdominios ativando deteccao automatica de Wildcard (-auto-wildcard) e exibindo ASN (-asn) e CDN (-cdn)
dnsx -l /cases/easm/raw_subdomains.txt \
  -a -resp \
  -auto-wildcard -wt 5 \
  -asn -cdn \
  -json -o /cases/easm/clean_enriched_dns.jsonl
```

## Limites e trade-offs
Note a diferença documentada no `README.md`: **`-wd exemplo.com.br`** ativa a filtragem manual de wildcard focada naquele domínio raiz, enquanto **`-auto-wildcard`** detecta dinamicamente domínios wildcard mesmo quando a lista de entrada `-l` contém dezenas de domínios raiz diferentes!

## Como verificar
Inspecione no arquivo JSONL (`-json`) os campos `"a"`, `"cname"`, `"asn"` e `"cdn"` gerados para cada subdomínio ativo.

## Conexões
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Veja também: ProjectDiscovery **`dnsx`**: Arquitetura do Toolkit DNS Multi-Propósito sobre `retryabledns`, Resolvers **UDP / TCP / DoH / DoT** e Modo **`-recon`**.
- [[dnsx-forca-bruta-subdominios-wordlists-placeholders-fuzz]] — Veja também: `dnsx`: Força Bruta de Subdomínios (`-d` + `-w`) e **Substituição por Marcador `FUZZ`** em Qualquer Posição do Nome DNS.
- [[naabu-exclusao-cdn-waf-exclude-cdn-port-threshold-protecao]] — Referência cruzada direta com naabu-exclusao-cdn-waf-exclude-cdn-port-threshold-protecao.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
