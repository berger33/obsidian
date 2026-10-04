---
id: software.devops.tranche19.001881
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/slackhq/nebula/master/README.md", "https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml", "https://github.com/slackhq/nebula"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nebula: arquitetura de rede overlay escalável baseada no Noise Protocol Framework, certificados PKI e `Lighthouses`

## Em uma frase
O **Nebula** (criado originalmente no Slack e mantido com a Defined Networking sob licença MIT) é uma ferramenta de rede overlay peer-to-peer mutuamente autenticada capaz de conectar desde poucas máquinas até dezenas de milhares de hosts em qualquer nuvem ou data center, baseando-se no **Noise Protocol Framework** (`ECDH` Curve25519/P256 e `AES-256-GCM`), certificados X.509 próprios (`nebula-cert`) e nós de descoberta chamados **Lighthouses**.

## Por que importa
Diferentemente de redes que dependem de um servidor de coordenação centralizado que mantém conexões ativas com todos os nós para distribuir listas de ACLs, o Nebula embute o endereço IP, a sub-rede e os **grupos de segurança (*groups*)** do host diretamente dentro do certificado assinado pela Autoridade Certificadora offline (`ca.key`).

## Como funciona
Quando dois nós Nebula iniciam um handshake Noise entre si, cada lado valida criptograficamente o certificado do outro contra o arquivo `ca.crt` local e descobre instantaneamente quais `groups` o par possui — aplicando o firewall do Nebula sem precisar consultar nenhum servidor central de políticas.

## Exemplo
```bash
nebula-cert ca -name "Acme Infrastructure CA"
nebula-cert sign -name "lighthouse1" -ip "192.168.100.1/24"
nebula-cert sign -name "app-server-1" -ip "192.168.100.10/24" -groups "servers,prod-web"
```

## Limites e trade-offs
O arquivo **`ca.key`** gerado por `nebula-cert ca` é o segredo mais crítico de toda a rede Nebula: ele **nunca** deve ser copiado para os nós nem para os Lighthouses; mantenha-o offline em cofre seguro e distribua apenas o certificado público `ca.crt`.

## Como verificar
Inspecione os metadados, grupos, sub-rede e validade de um certificado emitido executando `nebula-cert print -path app-server-1.crt`.

## Conexões
- [[nebula-cert-ca-sign-groups-subnets-curve-p256-fips]] — Veja também: Nebula PKI (`nebula-cert`): emissão de certificados com grupos de segurança, restrições de sub-rede e modo `P256` / FIPS 140-3.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
