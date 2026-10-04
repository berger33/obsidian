---
id: software.seguranca.tranche16.001504
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md", "https://raw.githubusercontent.com/greenbone/gvmd/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Varreduras Autenticadas (**Authenticated Scans — SSH, SMB/WMI, ESXi e SNMP**) e o Motor **`notus-scanner`** no Greenbone/OpenVAS

## Em uma frase
Qual é a diferença de profundidade e de impacto na rede entre uma **Varredura Não-Autenticada (*Black-Box Network Scan*)** e uma **Varredura Autenticada (*Authenticated Local Security Checks — LSC*)** no Greenbone/OpenVAS?

## Por que importa
Em uma varredura não-autenticada, o scanner vê apenas as portas expostas na rede e tenta deduzir vulnerabilidades por banners ou testes ativos. Já quando você associa **Credenciais SSH (chave privada Ed25519/RSA de um usuário sem privilégios)** para hosts Linux ou **Credenciais SMB** para hosts Windows ao seu Target, o OpenVAS faz login no servidor, coleta a lista exata de todos os pacotes instalados (`dpkg -l` / `rpm -qa` / Registro do Windows) e aciona o **`notus-scanner`**!

## Como funciona
O **`notus-scanner`** compara em milissegundos a lista de pacotes instalados contra os avisos de segurança oficiais da distribuição — detectando vulnerabilidades críticas em bibliotecas internas (`glibc`, `openssl`, `curl`, `sudo`, Kernel, `.NET`) **sem precisar enviar payloads de exploração pela rede e com zero falsos positivos de backport**!

## Exemplo
```bash
# Criar no servidor Linux alvo uma conta dedicada sem privilegios de root para Varredura Autenticada SSH do Greenbone/OpenVAS
useradd -m -s /bin/bash gvm-scanner
install -d -m 0700 -o gvm-scanner -g gvm-scanner /home/gvm-scanner/.ssh
```

## Limites e trade-offs
Sabia que para realizar 95% das verificações de pacotes instalados (`Local Security Checks` / `notus-scanner`) no Linux via SSH, **a conta `gvm-scanner` NÃO precisa de privilégios de `root` nem de `sudo`**? Qualquer usuário comum consegue ler a base de pacotes `rpm -qa` ou `dpkg -l` e a versão do kernel `uname -r`! Você só precisa conceder `sudo` (ou capacidades específicas) se também quiser rodar auditorias de conformidade **IT-Grundschutz / CIS Policies** que leem arquivos restritos como `/etc/shadow` ou `/etc/ssh/sshd_config`!

## Como verificar
Em ambientes Windows, garanta que o serviço *Remote Registry* esteja habilitado e que a conta de auditoria SMB tenha permissão de leitura administrativa (`LocalAccountTokenFilterPolicy` / grupo *Administrators* restrito ao IP do scanner via Windows Firewall).

## Conexões
- [[openvas-configuracao-alvos-targets-port-lists-alive-test-credenciais]] — Veja também: Configuração de **Targets, Port Lists e `Alive Test`** no Greenbone/OpenVAS: Evitando Falsos Negativos em Hosts com Firewall que Bloqueia `ICMP Echo`.
- [[openvas-perfis-varredura-full-and-fast-cve-scan-matching-version]] — Veja também: Perfis de Varredura (**`Full and fast`**, **`Host Discovery`**, **`System Discovery`**) e o **`CVE Scan` (`cve_scan_matching_version`)** no `gvmd`.
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Referência cruzada direta com openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa.
- [[openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds]] — Referência cruzada direta com openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
