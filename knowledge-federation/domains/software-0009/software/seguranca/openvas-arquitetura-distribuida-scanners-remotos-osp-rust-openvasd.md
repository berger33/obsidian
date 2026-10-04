---
id: software.seguranca.tranche16.001510
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

# Arquitetura Distribuída com **Scanners Remotos (`OSP` sobre mTLS)** e o Novo Motor em Rust (**`openvasd`**) em Containers (`ghcr.io/greenbone`)

## Em uma frase
Quando sua organização possui 5 segmentos de rede isolados por firewall (ex.: matriz, filial, DMZ, VPC de produção na AWS e rede PCI-DSS), abrir todas as 65.535 portas TCP/UDP no firewall entre um único scanner central e todas as 5 redes violaria completamente a segmentação Zero-Trust! Como escanear todas as 5 redes a partir de um único painel central do Greenbone (`gvmd` + `GSA`) sem abrir todas as portas nos firewalls?

## Por que importa
Implantando **Sensores Remotos (`ospd-openvas` + `openvas-scanner` ou o novo `openvasd` em Rust)** dentro de cada segmento de rede!

## Como funciona
O `gvmd` central se conecta a cada sensor remoto através de **uma única porta TCP autenticada por mTLS usando o protocolo `OSP` (*Open Scanner Protocol*)**: o `gvmd` envia a configuração da Task e a lista de alvos locais para o sensor daquela sub-rede, o sensor faz a varredura localmente dentro da VLAN e devolve apenas os resultados estruturados para o `gvmd` central!

## Exemplo
```bash
# Registrar no gvmd central um Scanner Remoto OSP autenticado por certificados mTLS (CA, certificado cliente e chave privada)
gvmd --create-scanner="Sensor-OSP-Rede-PCI" \
  --scanner-host=10.50.0.10 \
  --scanner-port=9390 \
  --scanner-type="OpenVAS" \
  --scanner-ca-pub=/var/lib/gvm/CA/cacert.pem \
  --scanner-key-pub=/var/lib/gvm/CA/clientcert.pem \
  --scanner-key-priv=/var/lib/gvm/private/CA/clientkey.pem
gvmd --verify-scanner="<UUID-DO-SCANNER>"
```

## Limites e trade-offs
Como destaca a seção *Rust Implementation* do `README.md` oficial do `greenbone/openvas-scanner`, a Greenbone desenvolveu no diretório `rust/` o novo daemon **`openvasd` em Rust**, projetado para substituir e unificar a pilha `ospd-openvas` + `notus-scanner` + controle do `openvas-scanner` em um único serviço seguro de memória e mais simples de operar em containers (`ghcr.io/greenbone/openvas-scanner:stable`)!

## Como verificar
Execute sempre **`gvmd --verify-scanner="<UUID>"`** após registrar um novo sensor OSP para validar o handshake mTLS e confirmar a versão do feed NVT carregada no sensor remoto.

## Conexões
- [[openvas-tuning-performance-max-checks-max-hosts-redis-memoria-redes]] — Veja também: Tuning de Performance e Concorrência no OpenVAS (**`max_hosts`**, **`max_checks`**, **`time_between_request`**) para Não Derrubar Redes ou Alvos Frágeis.
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Referência cruzada direta com openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa.
- [[openvas-protocolos-gmp-osp-automacao-gvm-cli-python-gvm-cicd]] — Referência cruzada direta com openvas-protocolos-gmp-osp-automacao-gvm-cli-python-gvm-cicd.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
