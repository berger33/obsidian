---
id: software.seguranca.tranche06.000547
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

# CAPEv2 Sandbox: Automação via **REST API v2** (`/apiv2/`, Autenticação por Token DRF, `throttling.py` e Integração com Cortex/MISP)

## Em uma frase
A **REST API v2** do CAPEv2 (`/apiv2/`, construída sobre *Django REST Framework*) expõe endpoints autenticados por token (`Authorization: Token <TOKEN>`) para submeter arquivos (`/apiv2/tasks/create/file/`) e URLs (`/apiv2/tasks/create/url/`), consultar status (`/apiv2/tasks/view/<id>/`), baixar relatórios JSON/MAEC/Lite (`/apiv2/tasks/report/<id>/`), recuperar PCAPs (`/apiv2/pcap/get/<id>/`) e baixar payloads extraídos.

## Por que importa
Permite que plataformas de SOAR, o analyzer `CAPE` do **Cortex/TheHive** ou gateways de e-mail submetam anexos suspeitos automaticamente, aguardem o término da detonação e injetem a configuração de C2 extraída de volta no caso de resposta a incidentes e no **MISP**.

## Como funciona
Para proteger o cluster de sandboxes contra sobrecarga, o módulo `web/apiv2/throttling.py` aplica limites de taxa por minuto/hora/dia (padrão `5/m` configurável em `api.conf` e ajustável individualmente por perfil de usuário no Django Admin `/admin/`).

## Exemplo
```bash
# Gerar token de API para conta de automacao do SOC e consultar o relatorio JSON de uma tarefa concluida
sudo -u cape poetry run python3 /opt/CAPEv2/web/manage.py drf_create_token soc_automation_bot

curl -sS -H "Authorization: Token ${CAPE_API_TOKEN}" \
  "http://127.0.0.1:8000/apiv2/tasks/report/1042/json/" | jq '{malscore: .malscore, detections: .detections, cape_cfg: .CAPE.configs}'
```

## Limites e trade-offs
A documentação oficial alerta que o antigo `utils/api.py` (porta `8090`) está **depreciado**; utilize sempre a API `/apiv2/` servida pelo stack web principal com autenticação por Token DRF habilitada e HTTPS.

## Como verificar
Valide que requisições sem o cabeçalho `Authorization: Token ...` para `/apiv2/tasks/create/file/` são rejeitadas com `HTTP 401/403` e ajuste a cota de throttling da conta do Cortex.

## Conexões
- [[capev2-assinaturas-comportamentais-rede-suricata-mitre-attack]] — Veja também: CAPEv2 Sandbox: Classificação Tripla — Assinaturas Comportamentais Python, Inspeção PCAP com **Suricata** e Mapeamento MITRE ATT&CK.
- [[capev2-anti-vm-hardening-kvm-qemu-acpi-smbios-human-interaction]] — Veja também: CAPEv2 Sandbox: Hardening Anti-Detecção de VM (*Anti-VM Cloaking* em KVM/QEMU, SMBIOS/ACPI, Artefatos de Usuário e *Interactive Desktop*).
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.
- [[thehive-orquestracao-cortex-analyzers-tlp-pap-opsec]] — Referência cruzada direta com thehive-orquestracao-cortex-analyzers-tlp-pap-opsec.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
