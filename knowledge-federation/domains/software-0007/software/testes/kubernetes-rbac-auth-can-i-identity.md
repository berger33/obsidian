---
id: software.testes.tranche09.000304
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://kubernetes.io/docs/reference/access-authn-authz/authorization/", "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kubernetes RBAC: verificar permissão com identidade e escopo

## Em uma frase
Autorização depende de verbo, recurso, namespace e identidade efetiva usada na requisição.

## Por que importa
Controladores Kubernetes reconciliam estado de forma assíncrona, então uma assertion instantânea sobre Pod isolado não representa necessariamente o resultado desejado. Um `can-i` executado com credencial de operador pode passar enquanto o ServiceAccount do workload continua sem acesso.

## Como funciona
Teste objetos e condições observáveis em cluster isolado, aguarde convergência com timeout e valide identidades e plugins que participam do comportamento. Rode consulta de autorização com identidade equivalente ao workload e repita para recurso e namespace corretos.

## Exemplo
O job testa se sua ServiceAccount pode listar ConfigMaps no namespace permitido e não pode ler Secrets de outro.

## Limites e trade-offs
Comportamento depende da versão, controller, scheduler e plugins instalados; dry-run do API server não prova execução de rede ou workload. `kubectl auth can-i` consulta autorização, mas não testa validação de objeto ou autorização adicional na aplicação.

## Como verificar
Capture usuário/grupos e namespace da credencial, confira binding e compare decisão autorizada e negada no API server.

## Conexões
- [[kubernetes-networkpolicy-plugin-enforcement-test]] — Veja também: Kubernetes NetworkPolicy: testar enforcement do plugin de rede.
- [[kubernetes-pdb-voluntary-disruption-test]] — Veja também: Kubernetes PDB: limitar disrupção voluntária em teste controlado.

## Fontes
- [Kubernetes — Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) — autorização por verbo, recurso, namespace e identidade; consultado em 2026-10-02.
- [Kubernetes — kubectl auth can-i](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/) — consultas de autorização do usuário corrente; consultado em 2026-10-02.
