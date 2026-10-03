---
id: software.seguranca.tranche08.000761
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

# OWASP **Amass**: Arquitetura de **External Attack Surface Management (EASM)**, Modelo de Grafo e **Open Asset Model (OAM)**

## Em uma frase
**OWASP Amass** (`owasp-amass/amass`, licença Apache-2.0, projeto Flagship da OWASP liderado por Jeff Foley / `@caffix`) é um framework de mapeamento de superfície de ataque externa (**EASM — *External Attack Surface Management***) e descoberta de ativos de rede via OSINT e reconhecimento ativo.

## Por que importa
Ao contrário de enumeradores simples que apenas cospem uma lista plana de subdomínios em texto, a arquitetura moderna do Amass modela toda a superfície externa como um **Grafo de Ativos e Relacionamentos** padronizado pela especificação **Open Asset Model (`owasp-amass/open-asset-model`)**: conectando entidades `Organization`, `AutonomousSystem` (ASN), `Netblock` (CIDR), `IPAddress`, `FQDN`, `TLS Certificate`, `WhoisRecord` e `Service`!

## Como funciona
Na arquitetura modular atual (v4+), o motor de coleta (**`amass enum`** e **`amass intel`**) persiste todos os ativos e arestas descobertos em um **Asset Database** (SQLite/PostgreSQL), que é então consultado e visualizado pela suíte de ferramentas **`oam-tools` (`oam_subs`, `oam_viz`, `oam_track`)**.

## Exemplo
```bash
# Verificar a versao do OWASP Amass e listar todas as fontes de dados OSINT suportadas pelo motor
amass -version
amass enum -list
```

## Limites e trade-offs
Por que modelar a superfície de ataque como um grafo OAM (`FQDN --[a_record]--> IPAddress <--[contains]-- Netblock <--[announces]-- ASN`) é muito mais poderoso do que uma lista de domínios? Porque ao descobrir que 15 subdomínios da empresa apontam para uma faixa `/24` de um ASN próprio, o Amass investiga o bloco CIDR inteiro (via PTR/TLS) e descobre novos domínios raiz da mesma empresa que você nem sabia que existiam!

## Como verificar
Execute `amass enum -list` para inspecionar o catálogo de fontes gratuitas e pagas disponíveis na sua versão.

## Conexões
- [[amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes]] — Veja também: OWASP Amass (`amass intel`): Descoberta de **Sementes Horizontais** — Mapeamento de **ASNs (`-asn`)**, Blocos **CIDR (`-cidr`)**, Organizações (`-org`) e *Reverse Whois*.
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Referência cruzada direta com amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
