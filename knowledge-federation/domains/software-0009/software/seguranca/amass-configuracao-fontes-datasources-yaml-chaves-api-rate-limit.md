---
id: software.seguranca.tranche08.000764
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

# OWASP Amass: Configuração de **`config.yaml` e `datasources.yaml`** — Chaves de API de Threat Intelligence, Rate Limits e `minimum_ttl`

## Em uma frase
Embora o OWASP Amass já consulte dezenas de fontes gratuitas sem configuração (como `crt.sh`, HackerTarget, RapidDNS, Wayback Machine, BGPView), seu poder máximo de descoberta passiva é desbloqueado ao configurar o arquivo **`datasources.yaml`** (e **`config.yaml`**) no diretório de configuração (`-config`).

## Por que importa
No `datasources.yaml`, a equipe de EASM cadastra chaves de API gratuitas ou corporativas (como Shodan, Censys, SecurityTrails, VirusTotal, Chaos, GitHub, PassiveTotal, URLScan, Hunter, WhoisXMLAPI), permitindo inclusive cadastrar **múltiplas chaves de API para a mesma fonte** (para que o Amass rotacione automaticamente entre elas!).

## Como funciona
Além disso, o atributo **`minimum_ttl`** (em minutos) por fonte instrui o banco de grafo do Amass a reutilizar os resultados em cache daquela API durante a janela configurada (ex.: `1440` minutos = 24h), economizando cota de API paga em execuções diárias!

## Exemplo
```yaml
# /cases/easm/datasources.yaml — Configuracao de fontes OSINT com multiplas chaves e cache minimum_ttl
datasources:
  - name: Censys
    ttl: 4320
    creds:
      account:
        apikey: "${CENSYS_API_ID}"
        secret: "${CENSYS_API_SECRET}"
  - name: Shodan
    ttl: 4320
    creds:
      account:
        apikey: "${SHODAN_API_KEY}"
  - name: VirusTotal
    ttl: 1440
    creds:
      account:
        apikey: "${VT_API_KEY}"
```

## Limites e trade-offs
Proteja o arquivo `datasources.yaml` com permissão **`chmod 0600`** e jamais faça commit dele com chaves de API reais no Git; use `-exclude` ou `-ef exclude.txt` quando quiser desativar fontes lentas específicas em uma execução rápida.

## Como verificar
Valide se o Amass reconheceu corretamente seu arquivo de configuração executando `amass enum -config /cases/easm/config.yaml -list`.

## Conexões
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Veja também: OWASP Amass (`amass enum`): Diferença Arquitetural entre os Modos **Passive (`-passive`)**, **Normal (DNS Validated)** e **Active (`-active`)**.
- [[amass-forca-bruta-recursiva-permutacoes-alterations-mascaras-hashcat]] — Veja também: OWASP Amass: Força Bruta DNS Recursiva (`-brute`, `-min-for-recursive`) e Geração Inteligente de **Permutações (`-alts`, `-awm` Máscaras Hashcat)**.
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Referência cruzada direta com amass-arquitetura-easm-owasp-open-asset-model-oam-grafo.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
