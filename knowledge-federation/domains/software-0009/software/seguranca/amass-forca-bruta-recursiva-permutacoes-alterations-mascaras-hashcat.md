---
id: software.seguranca.tranche08.000765
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/owasp-amass/amass/master/README.md", "https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md", "https://pkg.go.dev/github.com/owasp-amass/amass/v4"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP Amass: Força Bruta DNS Recursiva (`-brute`, `-min-for-recursive`) e Geração Inteligente de **Permutações (`-alts`, `-awm` Máscaras Hashcat)**

## Em uma frase
Um diferencial técnico do motor DNS do Amass frente a ferramentas de brute-force estáticas é a combinação de **Força Bruta Recursiva Automática (`-brute -min-for-recursive <N>`)** com **Alteração Inteligente de Nomes (`-alts` e máscaras `-awm`)**.

## Por que importa
Quando você ativa `-brute -min-for-recursive 2` e o Amass descobre que existem pelo menos `2` subdomínios sob uma sub-árvore (por exemplo, `api.prod.us-east.exemplo.com.br` e `auth.prod.us-east.exemplo.com.br`), o Amass percebe automaticamente que `*.prod.us-east.exemplo.com.br` é uma zona delegada/ativa e **inicia automaticamente uma nova rodada de força bruta recursiva sobre `prod.us-east.exemplo.com.br`**!

## Como funciona
Ao mesmo tempo, o motor de **Alterations (`-alts`)** aprende os padrões dos nomes já encontrados naquela empresa (ex.: se encontrou `api-dev-01`, ele gera automaticamente `api-dev-02`, `api-stg-01`, `api-prd-01`) e aceita **máscaras estilo Hashcat via `-awm`** (ex.: `-awm "dev?d?d"` para testar `dev00` a `dev99`)!

## Exemplo
```bash
# Executar enumeracao com forca bruta recursiva (quando >= 3 sub-rotulos existirem) e mascara de alteracao -awm
amass enum -d exemplo.com.br \
  -brute -min-for-recursive 3 \
  -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt \
  -alts -awm "stg?d" \
  -dir /cases/easm/amass_db -o /cases/easm/amass_recursive.txt
```

## Limites e trade-offs
Use **`-bl` / `-blf <blacklist.txt>`** para excluir da investigação recursiva sub-árvores de terceiros ou zonas dinâmicas de clientes (ex.: `-bl clientes.exemplo.com.br`), evitando gastar milhões de consultas DNS em zonas irrelevantes.

## Como verificar
Inspecione os subdomínios de 3º e 4º nível descobertos pela recursão e pelas permutações `-alts`.

## Conexões
- [[amass-configuracao-fontes-datasources-yaml-chaves-api-rate-limit]] — Veja também: OWASP Amass: Configuração de **`config.yaml` e `datasources.yaml`** — Chaves de API de Threat Intelligence, Rate Limits e `minimum_ttl`.
- [[amass-resolvers-dns-confiaveis-dns-qps-protecao-wildcard-poisoning]] — Veja também: OWASP Amass: Pool de **Resolvedores DNS Confiáveis (`-rf`, `-trf`)**, Limite de Taxa (`-dns-qps`, `-max-dns-queries`) e Detecção de **Wildcards / DNS Poisoning**.
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Referência cruzada direta com amass-arquitetura-easm-owasp-open-asset-model-oam-grafo.
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Referência cruzada direta com amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados.
- [[gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip]] — Referência cruzada direta com gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
