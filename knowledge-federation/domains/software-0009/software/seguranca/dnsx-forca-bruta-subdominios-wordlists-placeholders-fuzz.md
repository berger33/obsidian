---
id: software.seguranca.tranche09.000823
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

# `dnsx`: Força Bruta de Subdomínios (`-d` + `-w`) e **Substituição por Marcador `FUZZ`** em Qualquer Posição do Nome DNS

## Em uma frase
Além de validar listas prontas (`-l`), o `dnsx` é um motor de força bruta DNS de alta velocidade quando invocado com **`-d` / `-domain`** (um domínio, lista separada por vírgula ou arquivo de domínios) combinado com **`-w` / `-wordlist`**!

## Por que importa
Um recurso muito poderoso do `dnsx` para descobrir padrões de nomenclatura internos é o suporte ao marcador **`FUZZ`** dentro de `-d`: enquanto `dnsx -d exemplo.com.br -w palavras.txt` testa apenas o prefixo esquerdo (`<palavra>.exemplo.com.br`), passar **`dnsx -d "api-FUZZ.prod.exemplo.com.br" -w ambientes.txt`** substitui `FUZZ` no meio do nome DNS (`api-stg.prod.exemplo.com.br`, `api-hml.prod.exemplo.com.br`, `api-internal.prod.exemplo.com.br`)!

## Como funciona
Combinado com `-auto-wildcard` (ou `-wd exemplo.com.br`) e `-rl <queries_por_segundo>`, você executa permutações DNS cirúrgicas sem poluir a saída com wildcards.

## Exemplo
```bash
# Executar forca bruta DNS com marcador FUZZ no meio do rotulo filtrando wildcards e limitando a 500 req/s
dnsx -d "service-FUZZ.internal.exemplo.com.br" \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -a -cname -resp \
  -auto-wildcard \
  -rl 500 -t 100 \
  -o /cases/easm/dnsx_fuzz_services.txt
```

## Limites e trade-offs
Ao realizar força bruta DNS grande (`-w` com mais de 50.000 palavras), forneça sempre uma lista de resolvedores confiáveis via **`-r /cases/easm/resolvers.txt`** e configure **`-rl`** (`-rate-limit`) para não sofrer bloqueio por rate-limit no DNS local da sua máquina.

## Como verificar
Verifique as estatísticas de execução em tempo real adicionando a flag **`-stats`** durante o brute-force.

## Conexões
- [[dnsx-deteccao-asn-cdn-filtragem-wildcards-auto-wildcard-wd]] — Veja também: `dnsx`: Filtragem Automática de **DNS Wildcards (`-wd` / `-auto-wildcard`, `-wt`)** e Enriquecimento de **ASN (`-asn`) e CDN (`-cdn`)**.
- [[dnsx-varredura-reversa-ptr-cidr-asn-descoberta-hosts-internos]] — Veja também: `dnsx` **`-ptr` (`-resp-only`)**: Varredura de **DNS Reverso (`PTR` / `in-addr.arpa`)** a partir de Blocos CIDR e Números de **ASN (`AS...`)**.
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.
- [[amass-forca-bruta-recursiva-permutacoes-alterations-mascaras-hashcat]] — Referência cruzada direta com amass-forca-bruta-recursiva-permutacoes-alterations-mascaras-hashcat.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
