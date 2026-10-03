---
id: software.seguranca.tranche06.000546
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

# CAPEv2 Sandbox: Classificação Tripla — Assinaturas Comportamentais Python, Inspeção PCAP com **Suricata** e Mapeamento MITRE ATT&CK

## Em uma frase
O CAPEv2 classifica cada execução combinando três motores independentes: **(1)** scans **YARA** sobre o binário inicial e todos os payloads/dumps de memória extraídos, **(2)** inspeção de rede **Suricata** (e Zeek/JA3/HTTP/DNS) sobre o arquivo `dump.pcap` capturado na interface da VM e **(3)** **Behavioral Signatures** em Python que analisam a sequência de chamadas de API, arquivos, chaves de registro e mutexes.

## Por que importa
Um malware pode não ter nenhuma regra YARA estática conhecida ainda, mas se durante a execução ele apagar *Volume Shadow Copies* (`vssadmin.exe delete shadows /all /quiet`), injetar em `explorer.exe` e comunicar-se via TLS com um certificado autoassinado de Cobalt Strike detectado pelo Suricata, a classificação comportamental e de rede crava o veredito malicioso.

## Como funciona
As assinaturas comportamentais (`modules/signatures/`) mapeiam cada comportamento observado diretamente para técnicas **MITRE ATT&CK** (`ttp` IDs como `T1490` *Inhibit System Recovery*, `T1055` *Process Injection*, `T1547.001` *Registry Run Keys*) e atribuem um `malscore` numérico consolidado.

## Exemplo
```python
# Estrutura de uma Behavioral Signature customizada no CAPEv2 mapeada para MITRE ATT&CK (T1490)
from lib.cuckoo.common.abstracts import Signature

class DeletesShadowCopiesVssadmin(Signature):
    name = "deletes_shadow_copies_vssadmin"
    description = "Tenta excluir Volume Shadow Copies via vssadmin ou wmic (comportamento tipico de Ransomware)"
    severity = 3
    categories = ["ransomware"]
    ttp = ["T1490"]

    def run(self):
        for cmd in self.results.get("behavior", {}).get("summary", {}).get("executed_commands", []):
            if "shadow" in cmd.lower() and ("delete" in cmd.lower() or "resize" in cmd.lower()):
                self.data.append({"command": cmd})
                return True
        return False
```

## Limites e trade-offs
Mantenha o conjunto de regras do Suricata (`Emerging Threats Open / ET Pro`) atualizado no servidor host do CAPEv2 para que o módulo de processamento PCAP identifique padrões de tráfego C2 recentes.

## Como verificar
Consulte o campo `malscore`, `signatures` e `suricata.alerts` no relatório JSON da tarefa via `/apiv2/tasks/report/<id>/`.

## Conexões
- [[capev2-captura-amsi-powershell-dotnet-syscall-hooking-nirvana]] — Veja também: CAPEv2 Sandbox: Captura de Payloads **AMSI** (*Anti-Malware Scan Interface*), `.NET` / PowerShell / WSH e *Syscall Hooking* Anti-Evasão.
- [[capev2-integracao-api-rest-v2-automacao-submissao-thehive-misp]] — Veja também: CAPEv2 Sandbox: Automação via **REST API v2** (`/apiv2/`, Autenticação por Token DRF, `throttling.py` e Integração com Cortex/MISP).
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
