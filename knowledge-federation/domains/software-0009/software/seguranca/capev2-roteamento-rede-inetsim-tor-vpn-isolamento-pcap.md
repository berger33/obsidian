---
id: software.seguranca.tranche06.000549
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md", "https://capev2.readthedocs.io/en/latest/usage/api.html", "https://github.com/CAPESandbox/CAPE-parsers"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CAPEv2 Sandbox: Roteamento Por Tarefa (`route=inetsim`, `route=tor`, `route=vpn`, `route=none`) e Prevenção de Abuso Lateral

## Em uma frase
O daemon auxiliar **`rooter.py`** do CAPEv2 gerencia dinamicamente regras de roteamento `iptables`/`nftables` e tabelas `iproute2` no host Linux para permitir que o analista escolha, **por tarefa submetida**, como o tráfego de rede daquela VM convidada será tratado.

## Por que importa
Para malwares cujo payload já está embutido no binário, rodar com **`route=inetsim`** (simulando DNS, HTTP/HTTPS, SMTP e IRC localmente) é 100% seguro e fechado; porém, *downloaders* de primeiro estágio precisam baixar o segundo estágio do servidor real do atacante na internet para que o payload principal possa ser capturado e analisado.

## Como funciona
Ao selecionar `route=tor` ou `route=vpn_country_x` (ou `route=internet` via link dedicado sujo), o `rooter` cria regras de *Policy-Based Routing* para o IP da VM convidada durante a janela de detonação, bloqueando estritamente qualquer tráfego direcionado a faixas privadas RFC 1918 (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) e limitando conexões de saída de spam SMTP (porta `25`).

## Exemplo
```bash
# Submeter um downloader de 1o estagio roteando a saida da VM exclusivamente pelo tunel VPN isolado
curl -sS -X POST "https://cape.soc.internal.corp/apiv2/tasks/create/file/" -F "options=route=vpn_nl" \
  -H "Authorization: Token ${CAPE_NET_TOKEN}" \
  -F "file=@/cases/samples/stage1_downloader.docm" -F "timeout=180" | jq .
```

## Limites e trade-offs
Antes de habilitar qualquer rota externa (`tor`, `vpn` ou `internet`) no `routing.conf`, verifique com regras explícitas de firewall (`DROP` para RFC 1918 e link-local `169.254.0.0/16`) que a VM convidada não consegue alcançar a rede local do host nem metadados de nuvem.

## Como verificar
Teste dentro da VM convidada (em modo manutenção) que `ping 10.0.0.1` e conexões para a LAN interna são bloqueados pelo firewall do host.

## Conexões
- [[capev2-anti-vm-hardening-kvm-qemu-acpi-smbios-human-interaction]] — Veja também: CAPEv2 Sandbox: Hardening Anti-Detecção de VM (*Anti-VM Cloaking* em KVM/QEMU, SMBIOS/ACPI, Artefatos de Usuário e *Interactive Desktop*).
- [[capev2-integracao-memoria-volatility3-processamento-dumps-forenses]] — Veja também: CAPEv2 Sandbox: Geração de Dumps Completos de Memória RAM (`memory=1`) e Pós-Processamento Integrado com **Volatility 3**.
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.
- [[capev2-assinaturas-comportamentais-rede-suricata-mitre-attack]] — Referência cruzada direta com capev2-assinaturas-comportamentais-rede-suricata-mitre-attack.
- [[wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark]] — Referência cruzada direta com wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
