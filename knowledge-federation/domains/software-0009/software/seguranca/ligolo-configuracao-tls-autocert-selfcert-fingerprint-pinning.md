---
id: software.seguranca.tranche16.001562
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
fontes: ["https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md", "https://docs.ligolo.ng/Quickstart/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Segurança Criptográfica do Túnel Ligolo-ng: **Let's Encrypt (`-autocert`)**, Certificados Próprios (`-certfile`) e Pinning de **SHA-256 Fingerprint (`-selfcert` + `-accept-fingerprint`)**

## Em uma frase
Como autenticar e criptografar o túnel reverso TLS entre o `agent` e o `proxy` do **Ligolo-ng** impedindo ataques de interceptação (*Man-in-the-Middle*) mesmo quando você não possui um domínio público com Let's Encrypt?

## Por que importa
A documentação oficial (`Quickstart`) oferece **3 modos TLS no `proxy`**: **(1) `-autocert`** — solicita automaticamente um certificado TLS válido à **Let's Encrypt** (requer porta 80 acessível para validação ACME); **(2) `-certfile` e `-keyfile`** — usa seus próprios certificados X.509; e **(3) `-selfcert` combinado com Pinning de Fingerprint (`certificate_fingerprint` + `-accept-fingerprint`)**!

## Como funciona
No modo `-selfcert`, você executa o comando **`certificate_fingerprint`** no console do `proxy` para obter o hash SHA-256 exato do certificado gerado e inicia o `agent` passando **`-accept-fingerprint <HASH_SHA256>`**: o agente valida criptograficamente aquele hash exato no handshake TLS e aborta imediatamente se houver qualquer interceptação MITM no caminho!

## Exemplo
```bash
# Iniciar o Ligolo-ng Proxy com certificado autoassinado (-selfcert), obter o Fingerprint SHA-256 e conectar o Agent validando o Fingerprint
./proxy -selfcert -laddr 0.0.0.0:11601
./agent -connect 192.0.2.10:11601 -accept-fingerprint D005527D2683A8F2DB73022FBF23188E064493CFA17D6FCF257E14F4B692E0FC
```

## Limites e trade-offs
Preste atenção ao aviso de OPSEC destacado no `Quickstart` oficial sobre o modo **`-selfcert`**: por padrão, quando o `proxy` gera o certificado autoassinado com `-selfcert`, ele coloca o Common Name / Subject Name **`ligolo`** no certificado X.509 (facilmente detectado por regras de **Suricata / Snort 3 / Zeek**!). Para mudar o nome do domínio no certificado gerado, passe sempre **`-selfcert-domain cdn.exemplo-interno.com`** na inicialização do `proxy`!

## Como verificar
E como alerta o `Quickstart`: **nunca use `-ignore-cert`** fora de um laboratório local isolado, pois `-ignore-cert` desativa toda verificação de autenticidade do servidor TLS.

## Conexões
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Veja também: Arquitetura do **Ligolo-ng (`nicocha30/ligolo-ng`)**: Tunelamento de **Camada 3 (VPN-like)** com Interface **`TUN`** no Proxy e Pilha TCP/IP Userland (**Google `gVisor`**) no Agente.
- [[ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun]] — Veja também: Fluxo Operacional Completo no Console do Ligolo-ng (`v0.6+` / `v0.8+`): **`session`**, **`ifconfig`**, **`interface_create`**, **`interface_add_route`** e **`tunnel_start`**.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
