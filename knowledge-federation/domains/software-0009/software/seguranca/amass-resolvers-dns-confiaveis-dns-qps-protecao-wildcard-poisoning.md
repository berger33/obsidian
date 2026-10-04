---
id: software.seguranca.tranche08.000766
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

# OWASP Amass: Pool de **Resolvedores DNS Confiáveis (`-rf`, `-trf`)**, Limite de Taxa (`-dns-qps`, `-max-dns-queries`) e Detecção de **Wildcards / DNS Poisoning**

## Em uma frase
Quando você executa força bruta e validação de dezenas de milhares de subdomínios, dois problemas técnicos clássicos podem arruinar os resultados: **(1) Rate Limiting do seu servidor DNS local** (que passa a responder `SERVFAIL`/timeout, causando falsos negativos) e **(2) Resolvedores DNS Públicos Maliciosos ou com Ad-Blocking/NXDOMAIN Hijacking** (que retornam um IP falso em vez de `NXDOMAIN`, gerando milhares de falsos positivos!).

## Por que importa
Para resolver ambos com rigor de engenharia, o Amass separa os resolvedores em duas categorias: **`-r` / `-rf <resolvers.txt>`** (pool grande de resolvedores não-confiáveis para distribuir a carga pesada inicial com `-max-dns-queries` por resolvedor) e **`-tr` / `-trf <trusted_resolvers.txt>`** (pequeno conjunto de **Resolvedores Confiáveis**, como `1.1.1.1`, `8.8.8.8`, `9.9.9.9` ou seu próprio `unbound` local, onde toda resposta positiva é **re-validada** antes de entrar no grafo!).

## Como funciona
Adicionalmente, o motor de **Detecção Dinâmica de DNS Wildcard** do Amass sonda cada nível da hierarquia DNS com rótulos aleatórios em múltiplos resolvedores para descartar automaticamente zonas `*.dominio` wildcard.

## Exemplo
```bash
# Executar amass enum distribuindo consultas em um pool de resolvers (-rf) mas validando acertos nos Trusted Resolvers (-tr)
amass enum -d exemplo.com.br \
  -rf /cases/easm/public_resolvers_validated.txt \
  -tr 1.1.1.1,8.8.8.8,9.9.9.9 \
  -dns-qps 500 \
  -dir /cases/easm/amass_db -o /cases/easm/amass_verified.txt
```

## Limites e trade-offs
Nunca use uma lista de resolvedores DNS públicos baixada da internet (`resolvers.txt`) sem antes validá-la contra envenenamento de `NXDOMAIN` e confirmá-la com **`-tr 1.1.1.1,8.8.8.8,9.9.9.9`**; melhor ainda, suba uma instância local do resolvedor recursivo **`unbound`** que consulta diretamente os servidores autoritativos!

## Como verificar
Verifique que nenhum subdomínio inexistente (`teste-inexistente-999123.exemplo.com.br`) consta na saída validada.

## Conexões
- [[amass-forca-bruta-recursiva-permutacoes-alterations-mascaras-hashcat]] — Veja também: OWASP Amass: Força Bruta DNS Recursiva (`-brute`, `-min-for-recursive`) e Geração Inteligente de **Permutações (`-alts`, `-awm` Máscaras Hashcat)**.
- [[amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db]] — Veja também: OWASP Amass & **`oam-tools` (`oam_subs` / `amass db`)**: Persistência em Banco de Grafo (`-dir` / PostgreSQL) e Extração de Relações OAM.
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Referência cruzada direta com amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
