---
id: software.seguranca.tranche08.000763
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

# OWASP Amass (`amass enum`): Diferença Arquitetural entre os Modos **Passive (`-passive`)**, **Normal (DNS Validated)** e **Active (`-active`)**

## Em uma frase
Conforme documentado no guia oficial do usuário (`doc/user_guide.md`), o subcomando **`amass enum`** opera em três níveis distintos de interação com a rede que precisam ser escolhidos de acordo com o ROE (*Rules of Engagement*) da operação.

## Por que importa
No modo **Passive (`amass enum -passive -d exemplo.com.br`)**, o Amass **não envia nenhum pacote para os servidores do alvo nem realiza resolução DNS ativa dos achados**: ele apenas consulta fontes OSINT de terceiros (Certificate Transparency logs como `crt.sh`, arquivos web, APIs de threat intelligence) e registra os nomes reportados.

## Como funciona
No modo **Normal (padrão, sem `-passive` nem `-active`)**, o Amass coleta de todas as fontes OSINT **e** utiliza o pool de resolvedores DNS para validar que cada FQDN realmente existe (`A`/`AAAA`/`CNAME`/`TXT`/`SRV`/`MX`), descobrindo novos subdomínios a partir dos registros DNS retornados. Já no modo **Active (`amass enum -active -p 80,443,8080 -d exemplo.com.br`)**, ele vai além do DNS e **conecta diretamente aos ativos descobertos** para extrair certificados TLS, tentar transferência de zona DNS (`AXFR`), fazer *NSEC walking* DNSSEC e *web crawling*!

## Exemplo
```bash
# Executar enumeracao em modo Normal (OSINT + validacao DNS) com limite de 200 queries DNS por segundo e timeout de 30 min
amass enum -d exemplo.com.br \
  -dns-qps 200 \
  -timeout 30 \
  -dir /cases/easm/amass_db \
  -o /cases/easm/amass_enum.txt
```

## Limites e trade-offs
Atenção: como o modo `-passive` **não** faz resolução DNS, uma parte dos subdomínios retornados de logs históricos de Certificate Transparency de 5 anos atrás pode não existir mais hoje (`NXDOMAIN`); para alimentar scanners HTTP subsequentes (`httpx`), use o modo Normal ou filtre com um resolvedor DNS confiável.

## Como verificar
Inspecione o arquivo de log `-log /cases/easm/amass.log` para verificar se alguma fonte OSINT atingiu limite de taxa durante a execução.

## Conexões
- [[amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes]] — Veja também: OWASP Amass (`amass intel`): Descoberta de **Sementes Horizontais** — Mapeamento de **ASNs (`-asn`)**, Blocos **CIDR (`-cidr`)**, Organizações (`-org`) e *Reverse Whois*.
- [[amass-configuracao-fontes-datasources-yaml-chaves-api-rate-limit]] — Veja também: OWASP Amass: Configuração de **`config.yaml` e `datasources.yaml`** — Chaves de API de Threat Intelligence, Rate Limits e `minimum_ttl`.
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Referência cruzada direta com amass-arquitetura-easm-owasp-open-asset-model-oam-grafo.
- [[amass-resolvers-dns-confiaveis-dns-qps-protecao-wildcard-poisoning]] — Referência cruzada direta com amass-resolvers-dns-confiaveis-dns-qps-protecao-wildcard-poisoning.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
