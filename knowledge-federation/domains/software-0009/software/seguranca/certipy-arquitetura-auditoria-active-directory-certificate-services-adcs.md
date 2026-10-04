---
id: software.seguranca.tranche12.001131
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/ly4k/Certipy/main/README.md", "https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **Certipy (`ly4k/Certipy`)**: Auditoria, Enumeração e Testes de Segurança em **Active Directory Certificate Services (AD CS)**

## Em uma frase
Desde a publicação da pesquisa seminal *"Certified Pre-Owned"* (Will Schroeder e Lee Christensen, SpecterOps), o **Active Directory Certificate Services (AD CS — a infraestrutura de PKI corporativa da Microsoft)** tornou-se um dos vetores mais críticos de escalação de privilégio para `Domain Admin` e persistência furtiva em redes corporativas Windows!

## Por que importa
Desenvolvido em Python (`certipy-ad` no PyPI, construído sobre `impacket`, `ldap3`, `cryptography` e `asn1crypto`), o **Certipy** é o kit de ferramentas padrão da indústria (tanto para **Red Teams / Pentesters** quanto para **Blue Teams / Auditores de AD**) para descobrir Autoridades Certificadoras (CAs), enumerar *Certificate Templates* via LDAP/RPC e identificar todas as classes conhecidas de vulnerabilidades de AD CS (**`ESC1` a `ESC17`**, **Shadow Credentials** e **Golden Certificates**)!

## Como funciona
A CLI do Certipy é organizada em subcomandos especializados que cobrem todo o ciclo de auditoria de PKI no Active Directory: **`certipy find`** (enumeração e detecção de vulnerabilidades), **`certipy req`** (solicitação de certificados), **`certipy auth`** (autenticação Kerberos PKINIT / Schannel via certificado `.pfx`), **`certipy shadow`** (Shadow Credentials `msDS-KeyCredentialLink`), **`certipy ca`**, **`certipy template`**, **`certipy account`** e **`certipy relay`**!

## Exemplo
```bash
# Instalar o Certipy (certipy-ad) em um ambiente virtual isolado e verificar os subcomandos disponiveis
python3 -m venv .venv-certipy && source .venv-certipy/bin/activate
pip install certipy-ad
certipy --version
certipy --help
```

## Limites e trade-offs
O maior valor defensivo do Certipy é que **qualquer usuário comum do domínio (sem privilégio administrativo!)** consegue executar **`certipy find -vulnerable`** via LDAP padrão para gerar um relatório completo (texto, JSON e compatível com **BloodHound**) de todos os templates e configurações de CA vulneráveis na floresta Active Directory!

## Como verificar
Execute auditorias periódicas com `certipy find` sempre que novos Certificate Templates forem publicados na sua PKI corporativa.

## Conexões
- [[certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap]] — Veja também: Enumeração e Diagnóstico de AD CS com **`certipy find`**: Flag **`-vulnerable`**, Saída JSON/Stdout e Integração com **BloodHound**.
- [[certipy-vulnerabilidades-templates-esc1-esc2-esc3-san-eku-enrollment]] — Referência cruzada direta com certipy-vulnerabilidades-templates-esc1-esc2-esc3-san-eku-enrollment.
- [[hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket]] — Referência cruzada direta com hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket.

## Fontes
- [Certipy Official GitHub — Active Directory Certificate Services (AD CS) Attack & Enumeration Toolkit](https://raw.githubusercontent.com/ly4k/Certipy/main/README.md) — repositório oficial do Certipy cobrindo descoberta de CAs/Templates, identificação de vulnerabilidades ESC1–ESC17, Shadow Credentials e Golden Certificates; consultado em 2026-10-03.
- [Certipy Official Package & Architecture Specification (`pyproject.toml`)](https://raw.githubusercontent.com/ly4k/Certipy/main/pyproject.toml) — especificação técnica do pacote `certipy-ad` v5.1+ (`impacket`, `ldap3`, `cryptography`, `asn1crypto`, `neo4j`/BloodHound); consultado em 2026-10-03.
