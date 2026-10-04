---
id: software.seguranca.tranche09.000839
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod", "https://docs.projectdiscovery.io/tools/tlsx/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `tlsx`: Varredura TLS em **Portas Não-Padrão (`-p 443,8443,9443,6443,2379,636`)**, Controle de Concorrência (`-c`, `-delay`) e Proxy **`-proxy`**

## Em uma frase
O TLS não existe apenas na porta `443` de servidores web: em uma infraestrutura corporativa e Kubernetes moderna, as portas mais críticas protegidas por TLS são a **`6443` (Kubernetes API Server)**, **`2379` (etcd)**, **`10250` (Kubelet API)**, **`636` / `3269` (Active Directory LDAPS)**, **`9200` (Elasticsearch)**, **`5671` (RabbitMQ AMQPS)**, **`9093` (Kafka TLS)** e **`8443` / `9443` (Portais de Gerência)**!

## Por que importa
Como o `tlsx` opera diretamente na camada TLS (sem exigir que o protocolo superior seja HTTP!), você pode passar **`-p 443,636,2379,3269,6443,8443,9200,9443,10250`** (ou alimentar diretamente a saída `host:porta` do **Naabu**!) para extrair os certificados X.509 de bancos de dados, filas, controladores LDAP e clusters Kubernetes!

## Como funciona
E para auditar essas portas internas através de um pivô de rede, a flag **`-proxy socks5://127.0.0.1:1080`** encaminha todas as conexões TLS pelo túnel SOCKS5.

## Exemplo
```bash
# Inspecionar certificados TLS em portas de infraestrutura (LDAPS 636, Kubernetes 6443, etcd 2379, Kubelet 10250)
tlsx -l /cases/pentest/internal_hosts.txt \
  -p 443,636,2379,3269,6443,8443,10250 \
  -san -cn -so -ss -ex \
  -c 100 -timeout 5 \
  -json -o /cases/pentest/infra_tls_certs.jsonl
```

## Limites e trade-offs
Inspecionar o certificado da porta **`636` (LDAPS)** com o `tlsx` em um pentest interno revela imediatamente no `SAN`/`CN` o nome FQDN exato do controlador de domínio e o nome da Autoridade Certificadora interna do Active Directory (`AD CS`)!

## Como verificar
Ajuste `-c` (concorrência, padrão `300`) e `-delay` (ex.: `100ms`) ao sondar equipamentos internos para evitar picos de CPU por handshakes assimétricos.

## Conexões
- [[tlsx-auditoria-certificados-wildcard-wc-escopo-blast-radius]] — Veja também: `tlsx` **`-wc` (`-wildcard-cert`)**: Mapeamento de **Certificados Wildcard (`*.dominio`)** e Redução do *Blast Radius* de Chaves Privadas.
- [[tlsx-integracao-pipeline-subfinder-dnsx-naabu-tlsx-httpx-nuclei]] — Veja também: Pipeline de Descoberta Recursiva por Certificados: **`subfinder` -> `dnsx` -> `naabu` -> `tlsx -dns` -> `httpx` -> `nuclei`**.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.
- [[naabu-varredura-atraves-proxies-socks5-connect-payload-ipv6]] — Referência cruzada direta com naabu-varredura-atraves-proxies-socks5-connect-payload-ipv6.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
