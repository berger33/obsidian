---
id: software.seguranca.tranche16.001570
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

# Engenharia de Detecção (**Blue Team / SOC / NSM / EDR**) Contra o **Ligolo-ng**: Certificado TLS Default (`ligolo`), Multiplexador **`hashicorp/yamux`** e Telemetria de Processo

## Em uma frase
Como os engenheiros de detecção (**Suricata / Snort 3 / Zeek / RITA / EDR**) detectam um `agent` ou `proxy` do **Ligolo-ng (`nicocha30/ligolo-ng`)** operando na rede corporativa?

## Por que importa
Veja os **4 vetores de detecção técnica** que todo Blue Team deve implementar: **(1) Certificado TLS com Subject/Issuer `ligolo` (Modo `-selfcert` padrão)** — quando um operador inicia `./proxy -selfcert` sem alterar `-selfcert-domain`, o certificado TLS apresentado no handshake (ou inspecionado ativamente por scanners `tlsx` / `ZGrab2`) contém o nome literal `ligolo`!

## Como funciona
**(2) Detecção de Long Connection + Burst de Conexões Internas no Endpoint (EDR / Sysmon Event ID 3)**: um único processo não assinado em espaço de usuário mantém **1 conexão TLS persistente externa** (detectada pelo **RITA** como *Long Connection*) e repentinamente começa a abrir **centenas de conexões `TCP connect()` internas (`Sysmon Event ID 3`)** para a sub-rede local inteira (quando o operador roda Nmap/NetExec pelo túnel!); **(3) Porta padrão `11601/tcp`**; e **(4) Strings e Símbolos Go (`nicocha30/ligolo-ng`, `gvisor.dev/gvisor/pkg/tcpip`, `hashicorp/yamux`)** no binário!

## Exemplo
```bash
# Inspecionar um binario suspeito procurando as bibliotecas Go caracteristicas do Ligolo-ng (gvisor netstack e hashicorp/yamux)
strings -a /tmp/agente_suspeito | grep -E "(nicocha30/ligolo-ng|gvisor\.dev/gvisor/pkg/tcpip|hashicorp/yamux)"
```

## Limites e trade-offs
Olhe a correlação comportamental do **Vetor 2 (`Sysmon Event ID 3` / `Tracee` / `Tetragon` eBPF)** acima: é a detecção mais poderosa contra **qualquer** ferramenta de Pivoting (seja Ligolo-ng, Chisel ou Sliver SOCKS5)! Quando um processo que nunca faz varredura de rede (como um worker web ou binário em `/tmp/`) abre conexões TCP para mais de 20 IPs internos diferentes ou 50 portas diferentes em menos de 1 minuto, dispare um alerta imediato de **Internal Pivoting / Lateral Movement Scan** no SIEM!

## Como verificar
Com isso concluímos o módulo do **Ligolo-ng** na Tranche 16!

## Conexões
- [[ligolo-auditoria-active-directory-impacket-netexec-certipy-bloodhound-tun]] — Veja também: Executando Ferramentas de Auditoria **Active Directory (`NetExec`, `Impacket`, `Certipy`, `BloodHound CE`, `Responder`)** Nativamente sobre a Interface `TUN` do Ligolo-ng.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.
- [[ligolo-configuracao-tls-autocert-selfcert-fingerprint-pinning]] — Referência cruzada direta com ligolo-configuracao-tls-autocert-selfcert-fingerprint-pinning.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
