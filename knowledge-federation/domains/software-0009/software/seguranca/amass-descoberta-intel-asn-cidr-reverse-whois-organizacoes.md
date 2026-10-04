---
id: software.seguranca.tranche08.000762
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

# OWASP Amass (`amass intel`): Descoberta de **Sementes Horizontais** — Mapeamento de **ASNs (`-asn`)**, Blocos **CIDR (`-cidr`)**, Organizações (`-org`) e *Reverse Whois*

## Em uma frase
Antes de enumerar subdomínios de `exemplo.com.br` (*reconhecimento vertical*), um programa de gestão de superfície de ataque (EASM) ou Red Team precisa descobrir **todos os outros domínios raiz (`exemplo-pagamentos.com`, ` marca-adquirida.io`, `portal-interno.net`) e blocos de IP (ASNs/CIDRs) que pertencem à mesma corporação (*reconhecimento horizontal*)**!

## Por que importa
Conforme detalhado no `Users' Guide` oficial (`doc/user_guide.md`), o subcomando **`amass intel`** foi projetado especificamente para essa fase de inteligência horizontal: **(1)** pesquisar na tabela BGP global todos os Sistemas Autônomos da organização com **`amass intel -org "Nome da Empresa"`**; **(2)** extrair os prefixos CIDR e domínios hospedados em um ASN com **`amass intel -asn <numero>`**; e **(3)** descobrir domínios irmãos por *Reverse Whois* com **`amass intel -whois -d exemplo.com.br`**!

## Como funciona
E quando combinado com **`-active -cidr <bloco/mascara> -p 443,8443`**, o `amass intel` conecta nas portas TLS do bloco de IPs da empresa e extrai dos campos *Subject Common Name (CN)* e *Subject Alternative Name (SAN)* dos certificados X.509 todos os domínios raiz hospedados ali!

## Exemplo
```bash
# Descobrir Sistemas Autonomos (ASNs) de uma organizacao e mapear todos os dominios raiz anunciados nos blocos CIDR do ASN
amass intel -org "Example Corp"
amass intel -active -asn 64512 -p 443,8443 -o /cases/easm/root_domains_from_asn.txt
```

## Limites e trade-offs
Essa descoberta horizontal via `amass intel -asn` / `-whois` é onde as equipes de segurança encontram a chamada **Shadow IT e ativos de fusões e aquisições (M&A)**: empresas adquiridas há anos cujos domínios não usam o nome principal da marca, mas rodam na mesma infraestrutura e frequentemente estão fora do monitoramento do SOC.

## Como verificar
Alimente a lista de domínios raiz descobertos em `/cases/easm/root_domains_from_asn.txt` diretamente no `amass enum -df /cases/easm/root_domains_from_asn.txt`.

## Conexões
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Veja também: OWASP **Amass**: Arquitetura de **External Attack Surface Management (EASM)**, Modelo de Grafo e **Open Asset Model (OAM)**.
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Veja também: OWASP Amass (`amass enum`): Diferença Arquitetural entre os Modos **Passive (`-passive`)**, **Normal (DNS Validated)** e **Active (`-active`)**.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
