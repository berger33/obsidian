# MOC — Testes de Software (lote 0007)

Índice das 1055 notas substantivas redigidas até agora no lote `software-testes-2000-0001`, cuja meta é 2.000. As 1055 passaram pelo gate automatizado e têm revisão factual registrada: nove aprovadas pelo usuário e 1046 aprovadas por IA, sem converter estas últimas em aprovações humanas. Este mapa é navegação, não validação factual.

## Fundamentos, processo e testware
- [[test-objectives-context]] — selecionar objetivos conforme work product, riscos e contexto.
- [[testing-principles-contextual]] — usar os sete princípios como orientação contextual.
- [[error-defect-failure-root-cause]] — distinguir erro, defeito, falha e causa raiz.
- [[testing-vs-debugging]] — separar evidência de teste da investigação/correção.
- [[fundamental-test-activities]] — planejar, analisar, desenhar, implementar, executar e concluir.
- [[test-process-context-tailoring]] — adaptar atividades à situação, sem adotar receita única.
- [[testing-roles-management-and-testing]] — distinguir responsabilidades de gestão e função técnica.
- [[testware-artifacts]] — organizar os produtos de trabalho gerados pelas atividades.

## Teste estático, feedback e revisões
- [[static-testing-work-products]] — revisar work products e aplicar análise estática sem execução.
- [[static-vs-dynamic-testing]] — combinar evidências de abordagens complementares.
- [[early-frequent-stakeholder-feedback]] — obter feedback de stakeholders ao longo do SDLC.
- [[review-process-activities]] — estruturar planejamento, leitura, comunicação e tratamento de findings.
- [[review-types-formality-purpose]] — selecionar tipo de revisão conforme objetivo e risco.
- [[review-success-factors]] — preparar participantes e medir sucesso sem avaliar indivíduos.

## Níveis de teste
- [[test-levels-overview]] — comparar os cinco níveis do CTFL e seus objetivos.
- [[component-testing-isolation]] — avaliar componentes isolados.
- [[component-integration-testing-interfaces]] — examinar interações entre componentes.
- [[system-testing-requirements]] — verificar comportamento do sistema integrado.
- [[system-integration-testing-external-systems]] — testar interfaces com sistemas/serviços externos.
- [[acceptance-testing-validation]] — validar necessidades e readiness para uso/implantação.

## SDLC, manutenção e tipos de teste
- [[sdlc-impact-on-testing]] — relaciona o ciclo de vida ao escopo, timing e abordagem.
- [[testing-sequential-and-iterative-sdlc]] — compara cadência e sobreposição das atividades.
- [[good-testing-practices-across-sdlc]] — práticas de teste úteis em vários modelos.
- [[test-first-approaches-tdd-atdd-bdd]] — situa TDD, ATDD e BDD.
- [[test-driven-development]] — orienta código por testes escritos antes.
- [[acceptance-test-driven-development]] — deriva casos de critérios de aceitação.
- [[behavior-driven-development]] — comunica comportamento com exemplos.
- [[devops-testing-continuous-feedback]] — aproxima desenvolvimento, teste e operação.
- [[shift-left-testing]] — antecipa verificação sem retirar testes posteriores.
- [[testing-retrospectives-process-improvement]] — transforma experiência em melhorias acompanhadas.
- [[maintenance-testing-change-scope]] — considera risco e tamanho da mudança.
- [[maintenance-testing-triggers]] — cobre modificações, migrações e aposentadoria.
- [[testing-migrations-and-platform-upgrades]] — verifica ambiente e conversão de dados.
- [[retirement-testing-data-archival]] — valida arquivamento e recuperação.
- [[independence-of-testing-levels]] — compara níveis de independência.
- [[whole-team-approach-quality]] — compartilha responsabilidade quando apropriado.
- [[essential-skills-for-testers]] — mapeia competências para o trabalho de teste.
- [[functional-testing-quality-characteristics]] — verifica o que o sistema faz.
- [[nonfunctional-testing-quality-attributes]] — avalia como o sistema se comporta.
- [[confirmation-testing-after-fix]] — confirma correções.
- [[regression-testing-change-effects]] — identifica efeitos colaterais de mudanças.
- [[black-box-testing-specification-based]] — deriva testes da especificação.
- [[white-box-testing-structure-and-limits]] — usa a estrutura interna como base.
- [[experience-based-testing-techniques]] — organiza técnicas baseadas em experiência.
- [[error-guessing-experience]] — formula hipóteses a partir do histórico.
- [[checklist-based-testing]] — mantém condições focadas em uma lista.
- [[collaboration-based-test-approach]] — usa conversa para evitar defeitos.
- [[user-story-three-cs]] — organiza Card, Conversation e Confirmation.
- [[acceptance-criteria-as-test-conditions]] — trata critérios como condições testáveis.

## Papéis de revisão e suporte de ferramentas
- [[review-roles-responsibilities]] — distribui tarefas entre papéis da revisão.
- [[review-moderator-facilitator]] — facilita reuniões construtivas.
- [[review-scribe-recorder]] — registra findings e decisões.
- [[review-reviewer-role]] — examina work products e descreve anomalias.
- [[review-author-feedback-correction]] — cria e corrige o material revisado.
- [[review-leader-responsibility]] — responde pela organização geral.
- [[review-manager-resources]] — define prioridade e disponibiliza recursos.
- [[review-role-allocation-context]] — adapta a alocação ao risco e à formalidade.
- [[test-tool-categories]] — organiza categorias por atividade apoiada.
- [[test-tools-beyond-automation]] — inclui gestão, revisão e colaboração.
- [[test-tool-introduction-and-risk]] — planeja adoção, treinamento e mitigação.

## Isolamento, confiabilidade e regressão
- [[test-doubles-fakes-stubs-spies-mocks]] — escolher doubles conforme o papel e a forma de verificação.
- [[testes-hermeticos-dependencias]] — controlar e declarar dependências do ambiente.
- [[testes-flaky-determinismo]] — diagnosticar resultados inconsistentes.
- [[fixtures-pytest-ciclo-vida-escopos]] — controlar preparação, escopo e limpeza no pytest.
- [[snapshot-testing-jest-revisao]] — detectar mudanças de saída com snapshots revisados.
- [[regression-test-prioritization-risco-impacto]] — ordenar testes de regressão considerando impacto e risco.

## Seleção de dados e combinações
- [[particionamento-equivalencia-valores-fronteira]] — selecionar representantes de classes e exercitar limites.
- [[decision-table-testing-regras-condicionais]] — cobrir regras definidas por combinações de condições.
- [[combinatorial-testing-pairwise-t-way]] — cobrir interações t-way de parâmetros.

## Geração de casos, propriedades e sequências
- [[property-based-testing-hypothesis]] — expressar propriedades sobre entradas geradas.
- [[shrinking-contraexemplos-hypothesis]] — simplificar entradas que reproduzem uma falha.
- [[testes-stateful-model-based-hypothesis]] — gerar sequências de operações sobre sistemas com estado.
- [[state-transition-testing-coverage]] — derivar sequências e critérios de cobertura de modelos de estado.
- [[fuzzing-coverage-guided-libfuzzer]] — explorar caminhos com fuzzing guiado por cobertura.
- [[metamorphic-testing-oracle-relations]] — verificar relações entre execuções sem exigir oracle completo.
- [[differential-testing-comparacao-implementacoes]] — investigar divergências entre implementações equivalentes.
- [[test-oracles-resultados-esperados]] — escolher critérios para avaliar resultados de teste.

## Exploração e gestão de risco
- [[risk-based-testing-priorizacao-risco]] — concentrar esforço nos riscos de maior probabilidade e impacto.
- [[exploratory-testing-aprendizado-design-execucao]] — aprender, projetar e executar testes de forma integrada.
- [[session-based-testing-charters-debriefs]] — estruturar a exploração com missão, relato e debrief.

## Cobertura e eficácia das verificações
- [[cobertura-branches-statement-interpretacao]] — distinguir cobertura de statements e branches.
- [[mcdc-coverage-condicoes-independentes]] — verificar o efeito independente de condições lógicas.
- [[mutation-testing-eficacia-testes]] — verificar se a suíte detecta alterações de comportamento.
- [[piramide-testes-estrategia-contexto]] — distribuir testes conforme risco, custo e arquitetura.

## Acessibilidade, desempenho e resiliência
- [[teste-acessibilidade-automatizada-revisao-humana]] — combinar scanner com avaliação manual de tarefas acessíveis.
- [[performance-testing-modelagem-carga]] — modelar carga e critérios de desempenho.
- [[chaos-experiments-steady-state-blast-radius]] — testar resiliência com hipóteses e impacto controlado.

## Contratos de API e dados
- [[schema-based-api-testing-schemathesis-openapi]] — gerar casos de API a partir de um schema.
- [[test-data-privacidade-sinteticos]] — reduzir exposição e avaliar utilidade de dados de teste.

## Planejamento, controle e governança do teste
- [[test-planning-objetivos-escopo-comunicacao]] — alinhar objetivos, recursos, cronograma e comunicação.
- [[test-entry-exit-criteria]] — definir condições para iniciar e concluir atividades.
- [[test-effort-estimation-techniques]] — estimar esforço com métodos baseados em dados ou especialistas.
- [[test-case-prioritization-dependencies]] — ordenar casos considerando risco, cobertura e dependências.
- [[test-progress-metrics-relatorios-conclusao]] — monitorar resultados e comunicar progresso/encerramento.
- [[test-environment-configuration-management]] — manter versões e contexto reproduzíveis para testware.
- [[requirements-test-traceability]] — ligar base de teste, casos, resultados e defeitos.
- [[defect-report-reproducibility-severity-priority]] — registrar anomalias que possam ser reproduzidas e triadas.
- [[test-automation-investment-maintenance-risks]] — avaliar investimento, ROI e manutenção de automação.
- [[ci-feedback-testes-regressao]] — usar CI para fornecer feedback frequente e controlado.

## Desempenho: perfis de carga, percentis e testes de capacidade
- [[testes-latencia-percentis-thresholds]] — Defina limites de desempenho sobre percentis de latência, taxa de erros e objetivos de serviço, em vez de depender apenas da média.
- [[testes-correcao-funcional-sob-carga]] — Verifique respostas e invariantes funcionais enquanto o sistema atende carga, sem confundir sucesso HTTP isolado com correção do fluxo.
- [[testes-modelagem-carga-vus-taxa-chegada]] — Selecione um modelo aberto ou fechado de geração de carga de acordo com a pergunta que o teste pretende responder.
- [[testes-smoke-carga-minima-api]] — Use uma execução curta e de baixa carga para confirmar que o script, os endpoints principais e o ambiente respondem antes de testes maiores.
- [[testes-carga-media-perfil-trafego]] — Avalie o serviço com um perfil que represente tráfego típico, mix de operações e duração operacional relevante para a decisão.
- [[testes-stress-limite-capacidade]] — Aumente a carga de forma controlada acima do padrão esperado para observar degradação, ponto de saturação e recuperação.
- [[testes-spike-picos-abruptos]] — Simule uma subida rápida de carga para examinar se filas, autoscaling e dependências suportam mudanças abruptas e como o serviço se recupera.
- [[testes-soak-degradacao-temporal]] — Mantenha uma carga representativa por período prolongado para procurar degradação lenta que testes curtos não revelam.
- [[testes-breakpoint-rampa-carga]] — Aumente gradualmente a taxa ou concorrência para localizar a faixa em que o sistema deixa de cumprir critérios operacionais.
- [[testes-canary-validacao-telemetria]] — Use uma parcela controlada de tráfego real para observar se uma versão nova preserva sinais de saúde antes de ampliar o rollout.

## Acessibilidade: critérios WCAG e regressão multimodal
- [[teste-acessibilidade-navegacao-teclado]] — Verifique se ações e conteúdo operáveis podem ser alcançados e acionados sem mouse, respeitando o comportamento esperado de cada controle.
- [[teste-acessibilidade-foco-visivel-ordem]] — Examine se o foco de teclado permanece visível e percorre uma sequência que preserva significado e operabilidade.
- [[teste-acessibilidade-rotulos-erros-formulario]] — Confirme que controles têm rótulos e instruções associados e que erros identificam o campo, o problema e a forma de correção.
- [[teste-acessibilidade-nome-papel-valor]] — Valide se controles nativos e customizados expõem nome acessível, papel e estado coerentes com a função e com a interação atual.
- [[teste-acessibilidade-contraste]] — Meça contraste nas cores efetivamente renderizadas em cada estado relevante e confronte os resultados com o critério WCAG aplicável.
- [[teste-acessibilidade-reflow-zoom]] — Avalie se conteúdo e funcionalidade permanecem disponíveis quando o viewport é estreito ou o usuário amplia o conteúdo, sem exigir rolagem bidimensional indevida.
- [[teste-acessibilidade-wcag-target-size]] — Meça os alvos de entrada por ponteiro e avalie o requisito mínimo de tamanho ou as exceções de espaçamento definidas no critério.
- [[teste-acessibilidade-autenticacao-acessivel]] — Verifique se o processo de autenticação evita exigir uma função cognitiva sem alternativa ou apoio permitido pelo critério de acessibilidade aplicável.
- [[teste-acessibilidade-status-dinamico]] — Confirme que mensagens de sucesso, erro, progresso ou resultado de ação são programaticamente determináveis sem depender de uma mudança de foco.
- [[teste-acessibilidade-regressao-multimodal]] — Combine verificações automatizadas repetíveis com percursos manuais de teclado, zoom e tecnologia assistiva para detectar regressões de acesso.

## Segurança: autorização, sessão, entrada, headers e logs
- [[testes-autorizacao-horizontal-objetos]] — Verifique se uma conta autenticada consegue ler ou alterar somente os objetos pertencentes ao seu próprio escopo.
- [[testes-autorizacao-vertical-privilegios]] — Avalie se usuários de menor privilégio são impedidos de executar funções reservadas a papéis superiores, inclusive por chamadas diretas.
- [[testes-sessao-idle-timeout-replay]] — Verifique se a sessão expira por inatividade conforme a política e se um identificador invalidado não volta a autorizar requisições.
- [[testes-session-fixation-regeneracao-id]] — Confirme que uma sessão pré-autenticação não conserva o mesmo identificador depois que a identidade ou o privilégio da conta muda.
- [[testes-csrf-origem-token-cookie]] — Examine se uma operação que altera estado rejeita solicitações cross-site não autorizadas e se proteções são avaliadas no contexto real dos cookies.
- [[testes-validacao-input-reflected-xss]] — Siga entradas controladas até o contexto de saída e verifique se texto não confiável é exibido como dado, sem execução de conteúdo ativo.
- [[testes-ssrf-destino-url-egress]] — Avalie se uma funcionalidade que busca URLs limita destinos e protocolos a uma política explícita, sem alcançar recursos internos não autorizados.
- [[testes-autenticacao-rate-limit-enumeracao]] — Verifique que tentativas automatizadas são limitadas sem expor a existência de contas nem permitir que um teste cause bloqueio de usuários reais.
- [[testes-security-headers-browser]] — Inspecione cabeçalhos emitidos em respostas relevantes e valide se sua política corresponde à arquitetura e ao comportamento esperado do navegador.
- [[testes-logs-redaction-injection]] — Verifique que eventos necessários são registrados, dados secretos são excluídos ou mascarados e entradas não confiáveis não forjam registros.

## Confiabilidade, recuperação e rollout
- [[testes-degradacao-graciosa-invariantes]] — Introduza indisponibilidade ou lentidão de uma dependência e verifique se o serviço preserva operações essenciais ou comunica uma falha controlada.
- [[testes-load-shedding-limites-sobrecarga]] — Examine se, sob sobrecarga, o sistema limita trabalho e rejeita solicitações de forma controlada antes de comprometer todos os recursos.
- [[testes-retry-backoff-jitter-cascata]] — Valide que novas tentativas são limitadas, espaçadas e seguras para a operação, evitando multiplicar a carga quando uma dependência falha.
- [[testes-falha-dependencia-timeout-circuit-breaker]] — Simule timeout e falha de serviço dependente para confirmar orçamento de espera, abertura do circuit breaker e recuperação controlada.
- [[testes-restore-backup-integridade]] — Restaure um backup em ambiente isolado e confirme que dados e serviço podem ser recuperados, não apenas que o arquivo existe.
- [[testes-recuperacao-rto-rpo]] — Meça em exercício controlado se a recuperação atende objetivos declarados de tempo e perda máxima de dados, incluindo dependências necessárias.
- [[testes-canary-comparacao-baseline]] — Compare a versão canário e a versão estável por métricas e resultados sob condições suficientemente semelhantes antes de promover a mudança.
- [[testes-kubernetes-rolling-update-disponibilidade]] — Exercite uma atualização progressiva e confirme estado do Deployment, prontidão dos Pods e continuidade das operações esperadas.
- [[testes-rollback-versao-estado]] — Prove que uma implantação problemática pode ser revertida e que a versão anterior opera com o estado produzido durante a atualização.
- [[testes-probes-startup-liveness-readiness]] — Teste cada probe segundo seu propósito: permitir inicialização, reiniciar processo travado ou retirar temporariamente tráfego de instância não pronta.

## HTTP, contratos e integridade de dados
- [[testes-http-content-negotiation-vary]] — Verifique se o servidor escolhe uma representação compatível com Accept e outras preferências documentadas e se caches distinguem variantes quando necessário.
- [[testes-semantica-metodos-http-idempotencia]] — Verifique que métodos aceitos produzem os efeitos definidos pelo contrato HTTP, incluindo segurança, idempotência e resposta adequada a métodos não permitidos.
- [[testes-api-problem-details-rfc9457]] — Valide que erros publicados com Problem Details respeitam mídia, semântica HTTP e estrutura prevista no contrato, sem expor detalhes internos.
- [[testes-http-conditional-requests-etag]] — Exercite validators e precondições HTTP para detectar cache condicional e conflitos de atualização sem sobrescrever silenciosamente estado concorrente.
- [[testes-pagination-cursor-invariantes]] — Verifique que a navegação por cursor mantém ordem e cobertura previstas no contrato diante de limites, filtros e alterações concorrentes controladas.
- [[testes-api-rate-limit-429-retry-after]] — Valide a resposta à quota excedida e se clientes e caches respeitam o contrato de limitação de taxa sem retentar de forma agressiva.
- [[testes-contract-testing-compatibilidade-api]] — Combine validação de schema com interações que representam necessidades reais de consumidores para detectar incompatibilidades antes do deploy.
- [[testes-consumer-idempotency-duplicates]] — Entregue a mesma mensagem mais de uma vez e confirme que consumidor produz no máximo o efeito de negócio definido para aquele identificador.
- [[testes-consistencia-eventual-convergencia]] — Verifique se leituras eventualmente consistentes convergem dentro do comportamento e prazo operacional declarados, sem exigir visibilidade imediata não prometida.
- [[testes-database-integrity-reconciliation]] — Verifique invariantes de dados tanto no limite transacional do banco quanto em reconciliações independentes entre fontes ou projeções.

## Tranche 8 — frameworks e plataformas de teste (100 notas)

### Playwright
- [[playwright-fixture-ciclo-vida-isolamento]] — Playwright: ciclo de vida de fixtures por teste.
- [[playwright-fixture-worker-escopo-paralelismo]] — Playwright: fixtures de worker e estado compartilhado.
- [[playwright-autenticacao-storage-state-expiracao]] — Playwright: reutilização segura de estado autenticado.
- [[playwright-teardown-recursos-externos]] — Playwright: teardown confiável de recursos externos.
- [[playwright-mock-api-contrato-resposta]] — Playwright: mocks de API alinhados ao contrato.
- [[playwright-har-replay-cobertura-rede]] — Playwright: replay de HAR para cenários de rede.
- [[playwright-status-http-vs-falha-transporte]] — Playwright: distinguir erro HTTP de falha de transporte.
- [[playwright-retries-flaky-diagnostico]] — Playwright: retries como sinal de flakiness, não correção.
- [[playwright-paralelismo-dados-exclusivos]] — Playwright: dados exclusivos para testes paralelos.
- [[playwright-locators-assertions-web-first]] — Playwright: locators resilientes e assertions web-first.

### React Testing Library
- [[rtl-interacao-user-event-fluxo-realista]] — Testing Library: interações realistas com user-event.
- [[rtl-consultas-prioridade-role-name]] — Testing Library: priorizar consultas por papel e nome.
- [[rtl-async-findby-waitfor-condicao]] — Testing Library: aguardar estado assíncrono pela condição.
- [[rtl-waitfor-sem-efeito-colateral]] — Testing Library: manter waitFor sem efeitos colaterais.
- [[rtl-formulario-erro-associacao-label]] — Testing Library: validar formulários pela relação label-controle.
- [[rtl-render-customizado-provedores-contexto]] — Testing Library: render customizado com provedores.
- [[rtl-testar-resultado-nao-implementacao]] — Testing Library: verificar resultado em vez de detalhe interno.
- [[rtl-consulta-singular-ambiguidade]] — Testing Library: detectar consultas ambíguas.
- [[rtl-fetch-loading-empty-error-states]] — Testing Library: cobrir loading, vazio e erro de carregamento.
- [[rtl-cleanup-isolamento-renderizacao]] — Testing Library: limpeza e isolamento entre renders.

### Android
- [[android-test-pyramid-escopo-runner]] — Android: escolher escopo e runner de teste.
- [[android-instrumented-sincronizacao-sem-sleep]] — Android: sincronizar testes instrumentados sem sleeps fixos.
- [[android-uiautomator-fronteira-sistema]] — Android: UI Automator para fronteiras de sistema.
- [[android-compose-semantics-assertions]] — Android Compose: testar semântica e ações expostas.
- [[android-compose-clock-idle-animacoes]] — Android Compose: controlar clock e animações em testes.
- [[android-multiplas-telas-configuracao]] — Android: cobrir tamanhos de tela e configuração.
- [[android-process-death-restauracao-estado]] — Android: testar restauração após recriação do processo.
- [[android-permissoes-recusa-revocacao]] — Android: testar concessão, recusa e revogação de permissões.
- [[android-separar-teste-ui-de-regra]] — Android: não concentrar regras de negócio em teste de UI.
- [[android-test-flakiness-reproducao-dispositivo]] — Android: tornar falhas instrumentadas reproduzíveis.

### Flutter
- [[flutter-estrategia-unit-widget-integration]] — Flutter: distribuir testes entre unit, widget e integração.
- [[flutter-plugin-channel-mock-fronteira]] — Flutter: mockar canais de plugin sem alegar teste nativo.
- [[flutter-integration-dispositivo-fluxo]] — Flutter: desenhar testes de integração em dispositivo.
- [[flutter-widget-lista-rolagem-scrolluntilvisible]] — Flutter: testar listas longas sem assumir posição fixa.
- [[flutter-orientacao-layout-widget-test]] — Flutter: validar orientação retrato e paisagem.
- [[flutter-pumpandsettle-animacao-indefinida]] — Flutter: evitar pumpAndSettle em animações sem fim.
- [[flutter-finders-chaves-vs-texto]] — Flutter: escolher Finder por semântica, texto ou chave.
- [[flutter-testwidgets-pump-microtasks]] — Flutter: sincronizar pump e atualizações assíncronas.
- [[flutter-widget-erro-overflow-responsivo]] — Flutter: detectar overflow e conteúdo inacessível em widget tests.
- [[flutter-mocks-plugin-versus-device-regressao]] — Flutter: separar contrato simulado de regressão em dispositivo.

### Terraform
- [[terraform-validate-vs-test-provisionamento]] — Terraform: distinguir validate de terraform test.
- [[terraform-tests-mock-provider-escopo]] — Terraform: delimitar mocks de provider.
- [[terraform-test-run-apply-cleanup]] — Terraform: isolar testes que aplicam infraestrutura.
- [[terraform-variable-validation-contract]] — Terraform: testar validação de variáveis como contrato.
- [[terraform-check-block-nao-blocking]] — Terraform: interpretar check blocks sem tratá-los como preconditions.
- [[terraform-outputs-sensitive-testes]] — Terraform: testar outputs sem expor valores sensíveis.
- [[terraform-provider-lockfile-reprodutibilidade]] — Terraform: validar reprodutibilidade de providers.
- [[terraform-data-sources-outputs-mock-real]] — Terraform: testar data sources e outputs calculados.
- [[terraform-plan-assertions-estado-esperado]] — Terraform: verificar plano contra mudança de infraestrutura esperada.
- [[terraform-sandbox-isolamento-paralelo]] — Terraform: isolar sandboxes de testes paralelos.

### Kafka
- [[kafka-producer-idempotencia-retries-acks]] — Kafka: testar produtor idempotente e confirmação.
- [[kafka-ordering-partition-retries]] — Kafka: delimitar ordenação por partição.
- [[kafka-transactional-producer-consumer-read-committed]] — Kafka: testar transações com consumidor read-committed.
- [[kafka-offset-commit-proximo-registro]] — Kafka: verificar semântica de offset committed.
- [[kafka-at-least-once-consumidor-idempotente]] — Kafka: tornar efeitos do consumidor seguros contra redelivery.
- [[kafka-rebalance-processamento-em-curso]] — Kafka: testar rebalance com processamento em andamento.
- [[kafka-retry-dlq-erro-transitorio-permanente]] — Kafka: separar erro transitório de erro permanente.
- [[kafka-producer-callback-delivery-failure]] — Kafka: observar falhas de entrega no produtor.
- [[kafka-consumer-reset-start-offset]] — Kafka: testar offset inicial e política de reset.
- [[kafka-testcontainers-contrato-broker]] — Kafka: escolher broker de teste conforme contrato.

### Machine learning
- [[ml-feature-schema-contract-validacao]] — ML: validar schema de features antes do serving.
- [[ml-training-serving-skew-transformacao]] — ML: detectar divergência entre transformação de treino e serving.
- [[ml-data-leakage-split-temporal]] — ML: testar vazamento de informação entre splits.
- [[ml-reproducibilidade-seed-ambiente-artefatos]] — ML: tornar experimentos e artefatos reproduzíveis.
- [[ml-calibracao-limiares-decisao]] — ML: testar calibração e limiares de decisão.
- [[ml-monitoring-drift-feature-label]] — ML: monitorar drift sem confundir com queda de qualidade.
- [[ml-batch-online-paridade-predicoes]] — ML: comparar predição batch e online.
- [[ml-model-serving-fallback-timeout]] — ML: testar timeout e fallback de serving.
- [[ml-numerica-tolerancia-estabilidade]] — ML: definir tolerância para comparações numéricas.
- [[ml-canary-release-rollback-metricas]] — ML: liberar modelo por canário e critério de rollback.

### GitHub Actions
- [[gha-minimum-token-permissions]] — GitHub Actions: limitar permissões do token GITHUB_TOKEN.
- [[gha-script-injection-event-context]] — GitHub Actions: evitar injeção em scripts com contexto de evento.
- [[gha-pinning-third-party-actions]] — GitHub Actions: fixar e revisar actions de terceiros.
- [[gha-secrets-pull-request-forks]] — GitHub Actions: proteger secrets em pull requests externos.
- [[gha-concurrency-cancel-deployments]] — GitHub Actions: configurar concurrency sem cancelar release válida.
- [[gha-artifact-retention-provenance]] — GitHub Actions: reter artifacts sem perder proveniência.
- [[gha-environment-protection-gates]] — GitHub Actions: verificar gates de environment antes do deploy.
- [[gha-matrix-fail-fast-coverage]] — GitHub Actions: desenhar matrix que detecta incompatibilidade.
- [[gha-job-output-untrusted-artifacts]] — GitHub Actions: não confiar em artifacts de execução não privilegiada.
- [[gha-path-filters-ci-cobertura]] — GitHub Actions: testar path filters e caminhos de validação.

### Prometheus
- [[prometheus-alert-rule-unit-test-input-series]] — Prometheus: testar alert rules com séries controladas.
- [[prometheus-alert-for-pending-firing]] — Prometheus: cobrir estados pending e firing de alertas.
- [[prometheus-alert-labels-annotations-invariantes]] — Prometheus: validar labels e annotations de alertas.
- [[prometheus-recording-rule-expression-output]] — Prometheus: testar recording rules e série resultante.
- [[prometheus-rate-counter-reset]] — Prometheus: testar rate diante de reset de counter.
- [[prometheus-vector-vazio-vs-zero]] — Prometheus: diferenciar vetor vazio de valor zero.
- [[prometheus-aggregation-labels-cardinality]] — Prometheus: testar agregação e preservação de labels.
- [[prometheus-alert-no-data-scrape-failure]] — Prometheus: separar condição saudável de ausência de telemetria.
- [[prometheus-rule-test-boundary-time-window]] — Prometheus: cobrir fronteiras de janela em testes de regras.
- [[prometheus-promtool-ci-rule-validation]] — Prometheus: executar promtool no CI para regras versionadas.

### Docker
- [[docker-build-context-dockerignore-audit]] — Docker: auditar build context e .dockerignore.
- [[docker-multistage-runtime-minimo]] — Docker: verificar fronteira entre build stage e runtime.
- [[docker-base-image-digest-atualizacao]] — Docker: controlar base image e processo de atualização.
- [[docker-build-checks-lint-dockerfile]] — Docker: executar build checks para detectar erros de Dockerfile.
- [[docker-build-secrets-nao-arg-env]] — Docker: não inserir secrets em ARG, ENV ou layers.
- [[docker-container-nonroot-permissions]] — Docker: testar execução com usuário não privilegiado.
- [[docker-runtime-healthcheck-supervision]] — Docker: validar healthcheck sem confundi-lo com readiness.
- [[docker-image-test-smoke-entrypoint]] — Docker: testar a imagem final com smoke test.
- [[docker-cache-reproducibilidade-build]] — Docker: testar cache sem depender dele para correção.
- [[docker-image-sbom-provenance-release]] — Docker: associar imagem publicada a versão e proveniência.

## Tranche 9 — frameworks, protocolos e infraestrutura de teste (100 notas)

### Cypress
- [[cypress-test-isolation-indexeddb]] — Cypress: entender o alcance do test isolation.
- [[cypress-query-retry-sem-repetir-efeitos]] — Cypress: distinguir retryability de queries e efeitos.
- [[cypress-intercept-browser-vs-cy-request]] — Cypress: cy.intercept observa tráfego do app, não cy.request.
- [[cypress-register-intercept-before-trigger]] — Cypress: registrar intercept antes da ação que dispara a rede.
- [[cypress-stub-versus-real-server-coverage]] — Cypress: equilibrar stubs de rede e fluxo com servidor real.
- [[cypress-session-cache-validacao]] — Cypress: validar uma sessão restaurada por cy.session.
- [[cypress-cross-origin-cy-origin]] — Cypress: cruzar origens com cy.origin no mesmo teste.
- [[cypress-clock-timers-date]] — Cypress: controlar relógio sem mascarar espera externa.
- [[cypress-component-testing-boundary]] — Cypress: separar component testing de cobertura end-to-end.
- [[cypress-test-retries-diagnostico]] — Cypress: interpretar test retries como sinal de flakiness.

### Pact
- [[pact-consumer-request-as-sent]] — Pact: capturar a requisição que o cliente realmente envia.
- [[pact-matchers-consumer-relevant]] — Pact: escolher matchers por relevância para o consumidor.
- [[pact-not-functional-provider-test]] — Pact: não usar contrato como teste funcional do provider.
- [[pact-provider-verify-local-instance]] — Pact: verificar contracts contra instância local do provider.
- [[pact-provider-state-setup-per-interaction]] — Pact: preparar provider states determinísticos por interação.
- [[pact-provider-state-false-positive-params]] — Pact: evitar falso positivo por parâmetro de busca ignorado.
- [[pact-stub-below-request-validation]] — Pact: manter stubs abaixo da validação do request.
- [[pact-publish-version-verification-matrix]] — Pact: publicar versões e resultados para compatibilidade.
- [[pact-can-i-deploy-environment-context]] — Pact: testar can-i-deploy contra o ambiente real de destino.
- [[pact-webhook-provider-verification-feedback]] — Pact: tratar webhook como gatilho, não resultado de verificação.

### PostgreSQL
- [[postgresql-read-committed-snapshot-por-statement]] — PostgreSQL: testar snapshots no READ COMMITTED.
- [[postgresql-serializable-retry-serialization-failure]] — PostgreSQL: repetir transação após serialization failure.
- [[postgresql-mvcc-concurrent-read-write]] — PostgreSQL: testar visibilidade MVCC entre conexões.
- [[postgresql-unique-constraint-concorrencia]] — PostgreSQL: validar unicidade sob inserções concorrentes.
- [[postgresql-row-lock-skip-locked-queue]] — PostgreSQL: testar filas com FOR UPDATE SKIP LOCKED.
- [[postgresql-deadlock-sqlstate-retry]] — PostgreSQL: reproduzir deadlock e repetir operação inteira.
- [[postgresql-explain-analyze-execucao-side-effects]] — PostgreSQL: tratar EXPLAIN ANALYZE como execução.
- [[postgresql-sequence-valores-nao-gapless]] — PostgreSQL: não testar sequences como contador sem lacunas.
- [[postgresql-timestamptz-session-timezone]] — PostgreSQL: testar timestamptz com timezone explícito.
- [[postgresql-sqlstate-assertion-errors]] — PostgreSQL: afirmar SQLSTATE em vez de texto de erro.

### GraphQL
- [[graphql-validation-before-resolvers]] — GraphQL: validar operações antes de executar resolvers.
- [[graphql-variable-omitted-null-default]] — GraphQL: distinguir variável omitida de null explícito.
- [[graphql-non-null-null-propagation]] — GraphQL: testar propagação de null em campos non-null.
- [[graphql-partial-data-errors-path]] — GraphQL: aceitar data parcial quando um resolver falha.
- [[graphql-alias-fragment-response-shape]] — GraphQL: testar aliases e fragments pela forma da resposta.
- [[graphql-pagination-cursor-invariants]] — GraphQL: validar invariantes da paginação por cursor.
- [[graphql-dataloader-request-scope]] — GraphQL: testar batching sem compartilhar cache entre usuários.
- [[graphql-authorization-resolver-context]] — GraphQL: verificar autorização no caminho de execução.
- [[graphql-cache-control-private-identities]] — GraphQL: testar cache em respostas autenticadas.
- [[graphql-schema-change-compatibility]] — GraphQL: revisar mudanças de schema com operações consumidoras.

### Apple XCTest
- [[xctest-async-await-test-method]] — XCTest: usar async/await em testes assíncronos Swift.
- [[xctest-expectation-fulfillment-count]] — XCTest: controlar fulfillment e over-fulfillment de expectations.
- [[xctest-waiter-group-timeout]] — XCTest: aguardar grupo de expectativas com resultado explícito.
- [[xctest-ui-accessibility-identifiers]] — XCTest UI tests: selecionar controles por identificadores estáveis.
- [[xctest-app-launch-arguments-environment]] — XCTest UI tests: configurar o app por launch arguments.
- [[xctest-plans-matrix-configurations]] — Xcode test plans: variar configurações de execução intencionalmente.
- [[xctest-signpost-performance-metric]] — XCTest: medir intervalo instrumentado com signpost metric.
- [[xctest-order-independent-state-reset]] — XCTest: não depender da ordem dos métodos de teste.
- [[xctest-locale-device-configuration]] — XCTest: cobrir locale e device sem depender do simulador anterior.
- [[xctest-ui-wait-for-condition-not-sleep]] — XCTest UI tests: aguardar condição da interface, não sleep.

### Kubernetes
- [[kubernetes-job-completion-backoff]] — Kubernetes Job: testar conclusão e retries do controller.
- [[kubernetes-cronjob-no-exactly-once]] — Kubernetes CronJob: testar execução idempotente, não exactly-once.
- [[kubernetes-deployment-rollout-observed-state]] — Kubernetes Deployment: aguardar rollout e validar aplicação.
- [[kubernetes-networkpolicy-plugin-enforcement-test]] — Kubernetes NetworkPolicy: testar enforcement do plugin de rede.
- [[kubernetes-rbac-auth-can-i-identity]] — Kubernetes RBAC: verificar permissão com identidade e escopo.
- [[kubernetes-pdb-voluntary-disruption-test]] — Kubernetes PDB: limitar disrupção voluntária em teste controlado.
- [[kubernetes-hpa-eventual-convergence]] — Kubernetes HPA: testar convergência eventual de réplicas.
- [[kubernetes-configmap-env-vs-volume]] — Kubernetes ConfigMap: testar atualização por env e por volume.
- [[kubernetes-namespace-cleanup-isolation]] — Kubernetes: isolar testes de cluster por namespace descartável.
- [[kubernetes-service-endpoints-readiness]] — Kubernetes Service: testar endpoints prontos sem fixar IP de Pod.

### OpenTelemetry
- [[otel-inmemory-span-exporter-assertions]] — OpenTelemetry: inspecionar spans com exporter em memória.
- [[otel-span-error-status-exception]] — OpenTelemetry: testar exceção e status de span separadamente.
- [[otel-context-propagation-async-boundary]] — OpenTelemetry: preservar contexto em fronteira assíncrona.
- [[otel-resource-scope-instrumentation-identity]] — OpenTelemetry: distinguir resource de instrumentation scope.
- [[otel-inmemory-metrics-reader-aggregation]] — OpenTelemetry: testar agregação de métricas em memória.
- [[otel-histogram-buckets-boundaries]] — OpenTelemetry: testar histograma por limites e distribuição.
- [[otel-log-trace-correlation-context]] — OpenTelemetry: verificar correlação de logs com trace ativo.
- [[otel-cardinality-views-attribute-control]] — OpenTelemetry: testar cardinalidade e views de métricas.
- [[otel-test-provider-exporter-lifecycle]] — OpenTelemetry: isolar exporter e provider entre testes.
- [[otel-semconv-versioned-attributes]] — OpenTelemetry: versionar assertions de semantic conventions.

### pytest
- [[pytest-tmp-path-per-test-files]] — pytest: usar tmp_path para arquivos isolados por teste.
- [[pytest-tmp-path-factory-session-data]] — pytest: reservar tmp_path_factory para artefato caro compartilhado.
- [[pytest-yield-fixture-teardown-order]] — pytest: ordenar teardown de fixtures dependentes.
- [[pytest-fixture-scope-isolation]] — pytest: alinhar escopo de fixture ao ciclo de vida do recurso.
- [[pytest-parametrize-ids-values-reference]] — pytest: nomear parâmetros e proteger dados mutáveis.
- [[pytest-indirect-param-fixture-setup]] — pytest: usar indirect parametrization para setup configurável.
- [[pytest-autouse-fixture-hidden-side-effects]] — pytest: limitar efeitos ocultos de fixtures autouse.
- [[pytest-unittest-fixture-injection-limit]] — pytest: entender limites de fixtures em unittest.TestCase.
- [[pytest-monkeypatch-env-teardown]] — pytest: escopar monkeypatch de ambiente e dependências.
- [[pytest-xfail-strict-expected-failure]] — pytest: ativar strict para xfail não mascarar regressão.

### GitLab CI
- [[gitlab-rules-avoid-duplicate-pipelines]] — GitLab CI: testar rules para evitar pipelines duplicados.
- [[gitlab-merge-request-rules-main-config]] — GitLab CI: garantir que configuração principal habilita MR pipeline.
- [[gitlab-child-pipeline-source-parent-pipeline]] — GitLab CI: reconhecer CI_PIPELINE_SOURCE em child pipeline.
- [[gitlab-trigger-strategy-propagate-result]] — GitLab CI: propagar resultado do downstream ao pipeline pai.
- [[gitlab-needs-artifacts-explicit-dependency]] — GitLab CI: verificar que jobs recebem artifacts necessários.
- [[gitlab-cache-not-artifact]] — GitLab CI: não usar cache como evidência de build.
- [[gitlab-resource-group-serialize-deploy]] — GitLab CI: serializar deploys com resource_group.
- [[gitlab-rules-changes-path-coverage]] — GitLab CI: testar path rules para não pular validação compartilhada.
- [[gitlab-protected-variables-untrusted-pipeline]] — GitLab CI: evitar secrets em pipeline não confiável.
- [[gitlab-parallel-matrix-coverage]] — GitLab CI: validar combinações realmente cobertas por parallel matrix.

### Spring Boot
- [[spring-webmvctest-vs-springboottest]] — Spring Boot: escolher @WebMvcTest ou @SpringBootTest.
- [[spring-mockmvc-vs-random-port]] — Spring Boot: distinguir MockMvc de servidor em porta aleatória.
- [[spring-datajpatest-database-boundary]] — Spring Boot: delimitar @DataJpaTest e o banco usado.
- [[spring-testcontext-cache-dirties-context]] — Spring TestContext: controlar estado em ApplicationContext cacheado.
- [[spring-transactional-test-real-server-threads]] — Spring Boot: não presumir rollback do cliente em RANDOM_PORT.
- [[spring-testresttemplate-status-assertions]] — Spring Boot: afirmar status com TestRestTemplate explicitamente.
- [[spring-restclient-test-slice-mockserver]] — Spring Boot: usar @RestClientTest para cliente HTTP.
- [[spring-active-profiles-test-configuration]] — Spring Boot: declarar perfil de teste sem depender do ambiente local.
- [[spring-webtestclient-mock-vs-server]] — Spring Boot: testar WebTestClient em mock e servidor.
- [[spring-graphql-test-slice-boundary]] — Spring Boot: delimitar @GraphQlTest e integração GraphQL.

## Tranche 10 — frameworks, infraestrutura e ferramentas (notas 350–449)

### Selenium WebDriver: sincronização e interações no navegador
- [[selenium-explicit-wait-condicao-observavel]] — Uma espera explícita consulta uma condição definida até que ela seja verdadeira ou que o timeout configurado expire.
- [[selenium-nao-misturar-esperas-implicit-explicit]] — A espera implícita afeta buscas de elementos, enquanto a explícita aguarda uma condição específica definida pelo teste.
- [[selenium-locators-identidade-estavel]] — Locators traduzem uma propriedade observável do DOM em um alvo para interações WebDriver.
- [[selenium-findelement-find-elements-ausencia]] — findElement retorna um elemento correspondente e sinaliza ausência; findElements retorna uma lista, que pode estar vazia.
- [[selenium-stale-element-relocalizar-apos-render]] — Uma referência WebElement pode ficar obsoleta quando o nó original deixa de pertencer ao DOM ativo.
- [[selenium-frame-trocar-e-restaurar-contexto]] — O driver procura elementos no contexto de navegação atualmente selecionado; conteúdo em iframe requer troca explícita para o frame.
- [[selenium-nova-janela-diferenca-handles]] — WebDriver representa janelas e abas por handles únicos dentro da sessão e não distingue conceitualmente as duas formas.
- [[selenium-alert-wait-accept-dismiss]] — WebDriver expõe alertas, confirmações e prompts nativos por uma API específica após selecionar o alerta ativo.
- [[selenium-actions-sequencia-e-liberacao-input]] — Actions API encadeia comandos de dispositivos de entrada, como teclado, ponteiro e roda, para interações de baixo nível.
- [[selenium-elemento-interativo-validar-estado]] — Comandos de elemento incluem click, send keys, clear e ações apropriadas ao tipo do controle.

### JUnit 6.1.3: parametrização, ciclo de vida e execução
- [[junit-parametrized-test-casos-complementares]] — @ParameterizedTest executa um método repetidamente com argumentos fornecidos por uma fonte declarada.
- [[junit-methodsource-ordem-argumentos]] — MethodSource fornece os argumentos de cada invocação a partir de uma factory method compatível.
- [[junit-dynamic-test-factory-nao-e-caso]] — @TestFactory produz nós DynamicTest ou DynamicContainer em tempo de execução; a factory não é em si um caso de teste.
- [[junit-per-class-estado-compartilhado]] — O lifecycle padrão cria uma instância por método; PER_CLASS reutiliza uma instância para métodos da mesma classe.
- [[junit-parallel-opt-in-modos-e-sincronizacao]] — A execução paralela do Jupiter é opt-in; habilitar o parâmetro global não torna todos os nós concorrentes por padrão.
- [[junit-extension-parameter-resolver-explicito]] — Extensões Jupiter podem resolver parâmetros de métodos e construtores quando um ParameterResolver registrado declara suporte.
- [[junit-tempdir-escopo-e-limpeza]] — A extensão TempDir fornece diretório temporário a um campo ou parâmetro de teste.
- [[junit-tags-filtrar-testes-por-categoria]] — Tags identificam testes e podem ser usadas pelo runner para incluir ou excluir grupos durante uma execução.
- [[junit-condicional-nao-substitui-diagnostico]] — Anotações condicionais e @Disabled controlam se um teste é executado em determinado ambiente ou contexto.
- [[junit-repeated-test-invocacoes-nomeadas]] — @RepeatedTest agenda invocações repetidas de um método e pode expor o número atual e total pelo contexto de repetição.

### Mockito: isolamento de colaboradores e verificação de comportamento
- [[mockito-verificar-contrato-nao-roteiro-interno]] — verify verifica se uma interação esperada ocorreu e pode limitar a quantidade de chamadas.
- [[mockito-stubbing-nao-duplicar-verificacao]] — Stubbing define a resposta de um mock; verificar uma invocação stubada costuma ser redundante quando a saída do sistema já comprova seu uso.
- [[mockito-argumentcaptor-apos-verificacao]] — ArgumentCaptor guarda o argumento passado para uma chamada verificada para permitir assertions específicas sobre seus campos.
- [[mockito-matchers-consistencia-em-todos-argumentos]] — Quando um argumento de uma invocação usa matcher, todos os argumentos dessa mesma invocação precisam ser representados por matchers.
- [[mockito-strict-stubs-detectar-setup-morto]] — STRICT_STUBS ajuda a detectar stubs não utilizados e incompatibilidades entre argumentos configurados e invocações reais.
- [[mockito-lenient-apenas-no-stub-excepcional]] — Lenient permite que um stub escape de verificações estritas como unused stubbing ou argumento potencialmente incorreto.
- [[mockito-spy-metodo-real-e-efeitos-colaterais]] — Um spy delega chamadas não stubadas ao objeto real, diferentemente do mock que usa comportamento simulado.
- [[mockito-stubbing-consecutivo-modelar-retentativas]] — Stubbing consecutivo define respostas diferentes para chamadas subsequentes do mesmo método.
- [[mockito-nao-compartilhar-mock-mutavel-entre-testes]] — reset apaga stubbing e interações de um mock, enquanto clearInvocations limpa interações sem remover o comportamento configurado.
- [[mockito-junit-jupiter-lifecycle-explicito]] — MockitoExtension integra criação de mocks anotados e sessão Mockito ao lifecycle de testes Jupiter.

### Jest 30.5: execução assíncrona, mocks e snapshots
- [[jest-retornar-promise-para-aguardar-assercoes]] — Jest considera uma função assíncrona concluída quando sua Promise retornada resolve ou rejeita.
- [[jest-rejeicoes-async-com-rejects]] — Matchers .rejects permitem verificar o valor ou erro de uma Promise rejeitada e precisam ser retornados ou aguardados.
- [[jest-hooks-escopo-e-ordem]] — beforeAll, beforeEach, afterEach e afterAll organizam setup e cleanup no escopo em que são declarados.
- [[jest-beforeall-nao-compartilha-estado-entre-arquivos]] — beforeAll executa uma vez antes dos testes do escopo atual, não como banco de estado universal entre arquivos.
- [[jest-mock-function-calls-results-context]] — Mock functions registram chamadas, resultados, instâncias e contexto this para assertions sobre colaboração.
- [[jest-clear-reset-restore-mocks-diferencas]] — Clear apaga histórico, reset também substitui implementação configurada, e restore devolve implementação original quando a função é spy.
- [[jest-fake-timers-timers-pendentes-recursivos]] — Fake timers permitem avançar relógio JavaScript sem esperar o tempo real passar.
- [[jest-mock-modulos-esm-commonjs]] — O fluxo de mock de módulo depende do sistema de módulos e da ordem em que imports estáticos são avaliados.
- [[jest-snapshot-revisao-antes-de-atualizar]] — Snapshot armazena uma representação serializada para comparar execuções futuras e detectar mudanças de saída.
- [[jest-coverage-thresholds-nao-medir-qualidade-sozinhos]] — A configuração pode impor thresholds de cobertura globais ou para caminhos específicos e falhar quando o limite não é atingido.

### Vitest: mocks, isolamento e configuração de projetos
- [[vitest-vi-mock-hoisting-importacao]] — vi.mock é elevado pelo transformador do Vitest para executar antes dos imports estáticos do módulo de teste.
- [[vitest-domock-mock-runtime-import]] — vi.doMock registra um mock em runtime e não é içado como vi.mock.
- [[vitest-setupfiles-mocks-modulos-cache]] — Arquivos setupFiles são executados antes dos arquivos de teste e podem carregar módulos antes de um mock local.
- [[vitest-fake-timers-restaurar-relogio]] — vi.useFakeTimers substitui timers do ambiente selecionado até que o teste volte ao relógio real.
- [[vitest-setsystemtime-nao-disparar-timers]] — vi.setSystemTime altera a data percebida pelo código, mas não dispara por si só timers agendados.
- [[vitest-browser-mode-spy-namespace]] — Em Browser Mode, módulos ESM nativos têm namespace de importação que não pode ser substituído como um objeto mutável comum.
- [[vitest-projects-inheritance-opcoes-globais]] — Vitest Projects permite agrupar conjuntos de testes com opções próprias; projetos inline podem herdar configuração conforme extends.
- [[vitest-isolation-parallelism-tradeoff]] — Por padrão, o pool do Vitest isola arquivos de teste; configuração sem isolamento pode compartilhar estado de ambiente e módulos.
- [[vitest-coverage-provider-relatorio-declarado]] — Vitest suporta cobertura via provider nativo v8 ou instrumentação Istanbul, com configuração de reporters.
- [[vitest-snapshot-diff-revisao-intencional]] — Snapshots registram uma saída serializada e falham quando a nova saída difere do baseline salvo.

### Testcontainers para Java: readiness, ciclo de vida e isolamento
- [[testcontainers-startup-check-vs-readiness]] — Startup checks detectam o estado de inicialização do container; wait strategies aguardam uma condição de readiness do serviço.
- [[testcontainers-wait-endpoint-readiness-contract]] — A wait strategy pode observar condições diferentes, incluindo porta, resposta HTTP, healthcheck e logs.
- [[testcontainers-junit-static-vs-instance-containers]] — A extensão Jupiter associa containers estáticos ao ciclo de vida da classe e containers de instância ao lifecycle por teste.
- [[testcontainers-junit5-parallel-extension-limit]] — A integração JUnit Jupiter de Testcontainers documenta que execução paralela não é suportada pela extensão.
- [[testcontainers-manual-lifecycle-cleanup]] — Controle manual permite iniciar recursos fora do lifecycle automático de uma extensão e usá-los em escopo explícito.
- [[testcontainers-jdbc-url-configuracao-reprodutivel]] — O suporte JDBC permite solicitar bancos Testcontainers por URL jdbc:tc e associar o driver e módulo apropriados.
- [[testcontainers-reuse-opt-in-estado-persistente]] — Reusable Containers requer opt-in e configuração idêntica para que uma execução reutilize o recurso anterior.
- [[testcontainers-compose-espera-servico-especifico]] — A integração com Compose permite identificar serviços expostos e associar uma wait strategy ao serviço relevante.
- [[testcontainers-pinar-imagem-para-reprodutibilidade]] — Uma tag específica reduz mudanças inesperadas da imagem, enquanto um digest pode identificar exatamente o artefato resolvido.
- [[testcontainers-startup-parallel-independencia-recursos]] — Opções avançadas permitem reduzir tempo de inicialização de containers quando o setup possui serviços independentes.

### Grafana k6: modelagem de carga, métricas e thresholds
- [[k6-checks-precisam-threshold-para-falhar]] — Checks registram se uma condição observável passou, mas checks falhados não abortam nem reprovam sozinhos o teste.
- [[k6-thresholds-criterios-operacionais-pass-fail]] — Thresholds expressam condições de aprovação sobre métricas e podem afetar o resultado final de uma execução.
- [[k6-scenarios-executors-workload-nomeado]] — Scenario descreve como executar funções de teste e escolhe executor, duração, usuários ou taxa de iteração.
- [[k6-open-arrival-closed-vus]] — Executors baseados em VUs mantêm usuários virtuais que iniciam nova iteração após a anterior; arrival-rate agenda iterações por taxa.
- [[k6-dropped-iterations-capacidade-vus]] — Arrival-rate executors podem deixar de iniciar iterações quando não há VUs disponíveis ou o tempo máximo termina.
- [[k6-setup-teardown-dados-compartilhados]] — setup prepara dados antes dos cenários; seus dados JSON são copiados para cada VU e para teardown, não compartilhados como um objeto JavaScript mutável.
- [[k6-tags-segmentar-metricas-sem-alta-cardinalidade]] — Tags categorizam requests, checks, thresholds e métricas customizadas para filtragem e comparação.
- [[k6-threshold-por-tag-e-escopo-de-metrica]] — Threshold pode selecionar subconjuntos de métricas filtrando tags associadas aos samples.
- [[k6-sleep-pacing-representar-think-time]] — sleep(t) suspende o VU pelo número de segundos informado e pode representar think time quando a pausa fizer parte do workload.
- [[k6-browser-protocolo-e-experiencia-complementares]] — O módulo browser do k6 combina automação de navegador com métricas de desempenho frontend para jornadas sintéticas.

### OWASP ZAP: varredura passiva, ativa e automação segura
- [[zap-baseline-scan-passivo-sem-ataque]] — O Docker Baseline Scan realiza spidering e passive scanning, sem executar active attacks contra o alvo.
- [[zap-api-scan-definicao-e-active-scan]] — API Scan importa definições como OpenAPI, SOAP ou GraphQL e aplica varredura adaptada ao formato.
- [[zap-active-scan-autorizacao-e-ambiente]] — Active Scan envia requisições de ataque para identificar vulnerabilidades e pode alterar ou sobrecarregar o sistema alvo.
- [[zap-warnings-exitstatus-politica-ci]] — Automation Framework oferece job exitStatus para derivar o status da execução dos resultados configurados.
- [[zap-automation-framework-plano-yaml]] — Automation Framework executa jobs sequenciais a partir de um plano YAML com ambiente e configuração definidos.
- [[zap-passive-scan-wait-antes-do-relatorio]] — O job passiveScan-wait aguarda que o scanner passivo termine de processar a fila atual.
- [[zap-autenticacao-verificar-sessao-do-scan]] — ZAP suporta métodos de autenticação e verificações de sessão configurados no ambiente e no contexto.
- [[zap-alert-filter-excecao-com-justificativa]] — Alert Filters podem sobrescrever o risco de alertas de scans ativos e passivos; há regras globais e associadas a contexto.
- [[zap-relatorio-artefato-e-evidencia]] — O add-on de Report Generation produz relatórios em formatos configuráveis e tem suporte ao Automation Framework.
- [[zap-separar-passive-active-pipeline]] — Baseline passivo e varredura ativa têm efeitos e evidências diferentes e podem exigir agendas de pipeline diferentes.

### Schemathesis: geração baseada em schema e fluxos de API
- [[schemathesis-schema-inputs-e-checks]] — Schemathesis lê schema OpenAPI ou GraphQL para construir entradas e exercitar operações documentadas.
- [[schemathesis-fases-coverage-fuzzing-stateful]] — Data generation inclui estratégias e fases diferentes, como exemplos, coverage, fuzzing e execução stateful.
- [[schemathesis-valid-invalid-modes-contrato]] — Modos de geração podem focar entradas conformes ou violadoras do schema para testar aceitação e rejeição.
- [[schemathesis-shrinking-reproducao-falha]] — Shrinking busca reduzir uma entrada que reproduz uma falha para um caso menor e mais diagnóstico.
- [[schemathesis-stateful-links-sequencia-api]] — OpenAPI Links permite mapear explicitamente dados de uma resposta para parâmetros de outra operação e modelar relações stateful específicas.
- [[schemathesis-stateful-sem-link-nao-presumir]] — Schemathesis pode inferir conexões stateful por análise do schema OpenAPI, aprender relações de cabeçalhos Location no CLI e usar Links explícitos quando necessário.
- [[schemathesis-checks-server-error-schema-status]] — Checks centrais podem detectar erros do servidor, status não documentados e respostas incompatíveis com o schema.
- [[schemathesis-autenticacao-precedencia-e-sanitizacao]] — Schemathesis aceita autenticação por CLI, configuração ou mecanismo associado ao schema, com precedência definida pela ferramenta.
- [[schemathesis-pytest-parametrize-call-and-validate]] — A integração pytest parametriza testes pelas operações e oferece Case para executar e validar respostas.
- [[schemathesis-orcamento-exemplos-rate-limit]] — `generation.max-examples` limita casos da fase fuzzing por operação e sequências stateful; examples e coverage adicionam seus próprios casos.

### StrykerJS: mutation testing e interpretação de resultados
- [[stryker-dry-run-suite-original-passa]] — Stryker executa um dry run sem mutações antes de iniciar a avaliação de mutants.
- [[stryker-killed-survived-no-coverage]] — Killed indica que um teste falhou com o mutant ativo; survived e No coverage são undetected, enquanto Ignored é excluído intencionalmente da avaliação.
- [[stryker-threshold-break-falha-pipeline]] — Thresholds high e low classificam a pontuação, enquanto break pode fazer a execução terminar com erro abaixo do limite.
- [[stryker-coverage-analysis-custos-e-classificacao]] — Coverage analysis pode selecionar quais testes executar para cada mutant e distinguir categorias conforme dados do runner.
- [[stryker-incremental-resultados-cache-validade]] — Incremental mode reutiliza resultados quando arquivos mutados e testes não mudaram segundo o diff que o runner suporta.
- [[stryker-mutate-apenas-codigo-de-producao]] — A opção mutate seleciona arquivos e padrões sujeitos a alterações artificiais.
- [[stryker-ignore-mutant-justificado-e-visivel]] — Stryker permite excluir mutators, usar comentários disable ou plugins ignore para padrões específicos.
- [[stryker-static-mutants-pertest-requirement]] — StrykerJS exige coverageAnalysis perTest para ignoreStatic; mutants estáticos ignorados aparecem como Ignored e não contam no mutation score.
- [[stryker-timeout-investigar-runner-e-mutante]] — A configuração oferece limites temporais para processos de teste e execução de mutants.
- [[stryker-equivalent-mutant-score-interpretacao]] — Mutation score resume resultados de mutants no escopo selecionado, mas não classifica automaticamente equivalência semântica.

## Tranche 11 — frameworks, protocolos, carga e automação móvel (notas 450–549)

### REST Assured: contratos HTTP testáveis em Java
- [[restassured-given-when-then-fronteira]] — O padrão given/when/then organiza a especificação da requisição, a execução do HTTP e as expectativas sobre a resposta.
- [[restassured-request-specification-reuso-isolado]] — RequestSpecification agrupa dados de request que podem ser compostos e reaproveitados em várias chamadas.
- [[restassured-response-specification-contrato-comum]] — Uma response specification permite reutilizar assertions comuns para respostas de vários testes.
- [[restassured-path-query-parameters-distintos]] — Path parameters substituem segmentos nomeados do caminho; query parameters são enviados na parte de consulta da URL.
- [[restassured-object-mapping-dependencias-explícitas]] — REST Assured pode serializar objetos Java para JSON ou XML e desserializar respostas quando os mapeadores compatíveis estão disponíveis no classpath.
- [[restassured-jsonpath-extrair-depois-de-validar]] — JsonPath permite selecionar valores do corpo JSON da resposta para assertions ou etapas posteriores do teste.
- [[restassured-json-schema-validacao-opcional]] — REST Assured oferece matcher para validar um corpo JSON contra um schema, disponível pela integração de validação correspondente.
- [[restassured-filtros-logging-nao-e-wire-capture]] — Filters podem observar ou alterar request antes do envio e response antes das expectations; filtros também podem implementar logging ou autenticação.
- [[restassured-auth-por-caso-sem-credencial-em-log]] — REST Assured suporta esquemas de autenticação e configuração de credenciais por request.
- [[restassured-configuracao-global-reset-e-paralelismo]] — REST Assured expõe defaults estáticos como base URI, filtros e specifications que influenciam requests posteriores.

### WireMock: stubs HTTP, estados e diagnóstico de interações
- [[wiremock-mapping-request-response-contrato]] — Um stub WireMock associa condições de request a uma response configurada por código ou arquivo JSON.
- [[wiremock-urlpath-query-param-matching]] — WireMock permite comparar URL completa ou só o path e declarar query parameters separadamente.
- [[wiremock-json-body-matcher-estrutura]] — WireMock fornece matchers de corpo JSON que comparam conteúdo estruturado, além de comparação literal ou JSONPath.
- [[wiremock-priority-sobreposicao-stubs]] — Se múltiplos stubs combinam com uma request, a prioridade controla qual resposta é selecionada; números menores indicam prioridade maior.
- [[wiremock-scenario-maquina-de-estados]] — Um cenário WireMock representa uma máquina de estados simples; mappings podem exigir estado e mudar o estado após uma request.
- [[wiremock-verificacao-de-request-journal]] — O request journal mantém requests recebidas em memória para verificação e consulta após as chamadas do sistema sob teste.
- [[wiremock-unmatched-requests-near-miss]] — Requests sem mapping normalmente recebem 404 e podem ser consultadas como unmatched; near misses apontam mappings parecidos.
- [[wiremock-faults-para-resiliencia]] — WireMock pode simular falhas de transporte para observar como o cliente trata interrupções e respostas incompletas.
- [[wiremock-junit-extension-reset-por-teste]] — A extensão WireMock para JUnit Jupiter inicia e encerra servidor conforme lifecycle e, por padrão, reseta mappings e requests entre métodos.
- [[wiremock-response-template-dados-da-request]] — Response templating pode preencher partes da resposta com valores do contexto da request em vez de manter uma fixture fixa.

### Robot Framework 7.5: keywords, fixtures e dados de teste
- [[robot-test-case-keywords-observáveis]] — Um caso Robot Framework contém chamadas a keywords descritas nas seções de teste e executadas pelas bibliotecas importadas.
- [[robot-setup-teardown-escopo]] — Setups e teardowns podem ser definidos no nível de caso ou suite e executam keywords antes/depois da unidade configurada.
- [[robot-tags-selecao-sem-substituir-assertions]] — Tags podem classificar casos e orientar a seleção de testes durante a execução.
- [[robot-template-data-driven]] — Um test template transforma as linhas de argumentos de um caso em chamadas repetidas à keyword-template escolhida.
- [[robot-variaveis-escopo-prioridade]] — Robot Framework oferece variáveis de diferentes origens e escopos, e sua resolução depende da origem e do momento da definição.
- [[robot-resource-vs-library-import]] — Resource files compartilham user keywords e dados Robot; libraries fornecem keywords implementadas em Python ou outra integração suportada.
- [[robot-keyword-argumentos-e-conversao]] — User keywords podem receber argumentos nomeados ou posicionais e podem expor valores de retorno a outras keywords.
- [[robot-ignore-error-nao-esconder-falha]] — Run Keyword And Ignore Error captura falha de keyword e devolve status e mensagem, permitindo tratamento deliberado no fluxo.
- [[robot-wait-until-keyword-succeeds-idempotência]] — Wait Until Keyword Succeeds repete uma keyword em intervalo configurado até passar ou esgotar limite.
- [[robot-output-report-sensitive-data]] — Uma execução Robot gera output.xml e relatórios/logs configuráveis que ajudam a diagnosticar os casos executados.

### Cucumber e Gherkin: especificações executáveis sem ambiguidade
- [[cucumber-feature-scenario-executable-spec]] — Uma Feature agrupa cenários relacionados e cada Example ou Scenario descreve contexto, evento e resultado esperado em steps.
- [[cucumber-keywords-nao-fazem-parte-do-matching]] — A palavra Given, When ou Then dá semântica ao texto, mas não é usada por Cucumber para distinguir step definitions durante matching.
- [[cucumber-expressions-parametros-tipados]] — Step definitions podem usar Cucumber Expressions ou regular expressions e receber valores capturados como argumentos.
- [[cucumber-step-definitions-ambiguos-unicos]] — Cucumber precisa de uma definição única que corresponda ao texto de cada step; mais de uma correspondência impede execução inequívoca.
- [[cucumber-scenario-outline-examples-linhas]] — Scenario Outline é um template; suas steps recebem valores de placeholders e o outline executa uma vez para cada linha em Examples.
- [[cucumber-data-tables-argumento-final]] — Uma DataTable é passada como argumento multilinha final à step definition e pode ser convertida conforme sua forma e tipo.
- [[cucumber-doc-string-corpo-multilinha]] — Gherkin permite Doc Strings como argumento de step para passar texto longo, como JSON, GraphQL ou uma mensagem.
- [[cucumber-background-precondicao-compartilhada]] — Background define steps comuns executados antes dos cenários aplicáveis dentro da Feature ou Rule.
- [[cucumber-hooks-condicionais-com-tags]] — Hooks podem ser associados a expressões de tags para executar preparação ou limpeza em cenários selecionados.
- [[cucumber-tags-selecao-e-inclusao]] — Tags podem organizar features e cenários e selecionar subconjuntos de execução; expressões também podem restringir hooks.

### NUnit: parametrização, lifecycle e execução paralela
- [[nunit-test-async-await-task]] — NUnit aceita test methods async que retornam Task ou Task<T> e registra o resultado após a conclusão.
- [[nunit-testcase-cada-argumento-caso]] — TestCase fornece argumentos inline para um método parametrizado e permite que cada combinação seja descoberta como test case.
- [[nunit-testcasesource-fonte-enumeravel]] — TestCaseSource identifica campo, propriedade ou método que fornece argumentos para casos parametrizados.
- [[nunit-setup-teardown-por-caso]] — SetUp é chamado antes de cada test method e TearDown logo depois de cada test case na fixture.
- [[nunit-onetimesetup-hierarquia-fixture]] — OneTimeSetUp executa uma vez antes dos testes filhos da fixture; classes base e derivadas seguem ordem de herança documentada.
- [[nunit-setupfixture-escopo-namespace]] — SetUpFixture oferece setup e teardown únicos para fixtures pertencentes a namespace e subnamespaces na assembly.
- [[nunit-fixturelifecycle-instance-per-case]] — FixtureLifeCycle pode usar instância única por fixture ou instância nova por test case.
- [[nunit-parallelizable-nao-e-limite-de-workers]] — Parallelizable marca testes ou descendentes elegíveis para concorrência; LevelOfParallelism define o teto de workers da assembly.
- [[nunit-order-local-nao-sincroniza-conclusao]] — Order organiza quando testes ou fixtures começam dentro da suite que os contém; não ordena globalmente nem aguarda término anterior.
- [[nunit-testcontext-diagnostico-por-escopo]] — TestContext fornece dados do execution context e distingue contexto de caso em método/setup/teardown de contexto de fixture nos métodos one-time.

### xUnit.net v3: dados, fixtures e paralelismo
- [[xunit-fact-vs-theory-escopo]] — Fact representa um caso individual; Theory associa a um método conjuntos de dados que produzem invocações parametrizadas.
- [[xunit-inline-data-casos-visíveis]] — InlineData fornece argumentos constantes para Theory e cada linha representa um caso executável.
- [[xunit-memberdata-classdata-provedor-tipado]] — Theories podem obter dados de membros ou classes provedoras, separando matriz de argumentos da lógica do teste.
- [[xunit-constructor-dispose-instancia-por-teste]] — xUnit cria instância nova da classe de teste para cada test que executa; constructor e Dispose oferecem preparação e limpeza por instância.
- [[xunit-class-fixture-compartilhar-recurso]] — IClassFixture compartilha uma instância de fixture entre os testes de uma classe e a descarta depois da classe.
- [[xunit-collection-fixture-serializar-recurso]] — Collection fixtures compartilham fixture entre classes associadas à mesma collection; classes na collection deixam de executar paralelamente entre si.
- [[xunit-async-lifetime-teardown]] — xUnit oferece interfaces de lifecycle assíncrono para inicialização e limpeza; suportes de DisposeAsync diferem entre v2 e v3.
- [[xunit-paralelismo-por-collection-isolar]] — No modo collections, testes de uma collection não rodam em paralelo entre si, mas collections distintas podem concorrer.
- [[xunit-outputhelper-saida-associada]] — ITestOutputHelper fornece saída associada ao test case, enquanto Console e Trace são recursos compartilhados do processo.
- [[xunit-assert-throws-tipo-exato]] — Assert.Throws e variantes assíncronas capturam exceção da operação e permitem verificar tipo e conteúdo da falha.

### Locust: cenários de usuário e geração de carga Python
- [[locust-httpuser-nao-e-browser]] — HttpUser oferece client HTTP e mantém cookies, mas não renderiza HTML nem carrega automaticamente recursos da página como browser.
- [[locust-task-weights-probabilidade]] — Decorador @task com peso faz Locust escolher tarefas com frequência relativa entre as opções disponíveis do usuário.
- [[locust-wait-time-pos-task-nao-rps]] — wait_time é aplicado após a execução de uma tarefa; ausência de wait_time inicia a próxima task assim que a atual termina.
- [[locust-on-start-stop-lifecycle]] — on_start e on_stop são callbacks por instância de User que permitem iniciar e encerrar contexto do usuário simulado.
- [[locust-request-name-cardinalidade]] — O parâmetro name do client pode agrupar requests com paths ou query values diferentes sob um nome de estatística comum.
- [[locust-catch-response-validacao-manual]] — Cliente HTTP de Locust permite inspecionar resposta no bloco catch_response e decidir manualmente se a chamada conta como sucesso ou falha.
- [[locust-taskset-sequencia-de-tarefas]] — TaskSet organiza conjunto de tarefas e pode delegar para subtasksets; SequentialTaskSet expressa sequência declarada quando a jornada requer ordem.
- [[locust-loadtestshape-tick]] — LoadTestShape permite controlar usuários e spawn rate através de tick, que retorna a população desejada e pode terminar com None.
- [[locust-distributed-master-worker]] — Em execução distribuída, master coordena interface e spawn/stop; workers executam Users e enviam estatísticas ao master.
- [[locust-fast-httpuser-gerador-versus-alvo]] — FastHttpUser pode reduzir overhead de cliente HTTP quando Locust precisa gerar uma taxa alta de requests.

### Apache JMeter: planos de teste e carga reproduzível
- [[jmeter-threadgroup-threads-independentes]] — Cada thread de um Thread Group executa o plano de teste de forma independente e pode representar uma conexão/usuário concorrente.
- [[jmeter-timer-before-samplers-scope]] — Timer é processado antes de cada sampler dentro do escopo hierárquico, e múltiplos timers podem acumular atraso.
- [[jmeter-assertion-aplica-por-escopo]] — Assertions são executadas após samplers no escopo onde aparecem e verificam campos de request/response configurados.
- [[jmeter-csv-dataset-dados-por-thread]] — CSV Data Set Config lê registros em variáveis e normalmente fornece linhas diferentes às threads do plano.
- [[jmeter-thread-variables-properties-compartilhamento]] — Variáveis de JMeter têm escopo de thread, enquanto properties são compartilhadas entre threads do processo.
- [[jmeter-cli-para-carga-gui-para-debug]] — Manual recomenda GUI para criar/debuggar plano e CLI mode para load test com menor overhead de interface.
- [[jmeter-execution-order-processors]] — JMeter processa elementos da árvore em ordem definida, com configuration elements e preprocessors antes do sampler e postprocessors/assertions depois.
- [[jmeter-listeners-impacto-gerador]] — Listeners exibem, salvam ou processam resultados e podem consumir recursos do gerador conforme volume e formato.
- [[jmeter-transaction-controller-unidades-medicao]] — Transaction Controller agrupa samplers em transação e pode produzir sample agregado conforme modo configurado.
- [[jmeter-testplan-versioned-results]] — Plano JMX e properties determinam execução; registrar apenas arquivo de resultado não permite reproduzir configuração de carga.

### Gatling: cenários, sessão e critérios de performance
- [[gatling-scenario-exec-sequencia]] — Um ScenarioBuilder encadeia ações com exec; requests e funções executadas no cenário seguem a sequência declarada.
- [[gatling-session-estado-por-virtual-user]] — Session representa o estado de um virtual user e carrega atributos ao longo das ações do scenario.
- [[gatling-feeder-dados-variados-cache]] — Feeder fornece records aos virtual users por meio de feed e os atributos passam para Session.
- [[gatling-check-saveas-apos-sucesso]] — Checks validam request/response e podem extrair um valor para Session; saveAs só é efetivo quando check passa.
- [[gatling-assertions-criterios-de-simulacao]] — Assertions na Simulation definem critérios sobre estatísticas globais ou escopos como requests/grupos.
- [[gatling-open-closed-injection-model]] — Perfis open injetam usuários por taxa de chegada; closed model define concorrência de usuários cuja duração influencia novas iterações.
- [[gatling-groups-agregacao-por-jornada]] — Groups agrupam ações do usuário e permitem observar estatísticas relativas a uma parte nomeada do scenario.
- [[gatling-pauses-e-pacing]] — Pause modela intervalo entre ações do scenario; injection controla chegada/concorrência inicial de virtual users.
- [[gatling-protocol-config-comum]] — Protocol configuration reúne base URL, headers e opções compartilhadas que podem ser associadas a um ou mais cenários.
- [[gatling-session-debug-fora-da-carga]] — Session pode ser inspecionada durante desenvolvimento para diagnosticar feeders, expressões e check failures.

### Appium: sessões e automação móvel multiplataforma
- [[appium-driver-instalacao-modular]] — Appium separa o servidor central de drivers que implementam automação por plataforma e precisam ser instalados para criar sessões.
- [[appium-capabilities-prefix-vendor]] — Capabilities são parâmetros key-value de criação de sessão e não podem ser alteradas durante seu lifecycle; capabilities não padrão usam prefixo vendor como appium:.
- [[appium-automationname-seleciona-driver]] — appium:automationName indica qual driver deve executar comandos da sessão.
- [[appium-context-native-webview]] — Contexts representam modos de automação que o driver implementa; API permite listar, ler contexto atual e trocar para outro nome disponível.
- [[appium-session-finally-delete]] — Quickstart abre session remota e chama deleteSession ao concluir interação; lifecycle da sessão é responsabilidade do cliente de teste.
- [[appium-w3c-actions-vs-comandos-driver]] — Appium oferece comandos W3C e extensões específicas do driver; migrações podem remover endpoints touch legados e apontar alternativas.
- [[appium-parallel-device-identidade-ports]] — Capabilities como udid identificam dispositivo alvo; drivers também podem requerer portas e recursos distintos para sessões simultâneas.
- [[appium-uiautomator2-android-boundary]] — UiAutomator2 é driver oficial para Android e documenta capabilities, comandos e requisitos que não são universais a todo Appium.
- [[appium-xcuitest-ios-boundary]] — XCUITest é driver oficial para apps iOS e seus requisitos dependem do host, toolchain Apple e configuração da sessão.
- [[appium-locators-acessibilidade-contrato]] — Drivers expõem estratégias de locator dependentes da plataforma, incluindo identificadores de acessibilidade ou recursos nativos.

## Tranche 12 — frameworks, propriedades e ferramentas de teste (IDs 550–649; revisão factual por IA registrada)

### Playwright Test — projetos, servidores e artefatos de execução

550. [[playwright-projects-browser-matrix]] — Um projeto nomeado combina os testes com opções de execução, como browser, dispositivo ou ambiente.
551. [[playwright-project-dependencies-setup]] — Uma dependência de projeto permite executar testes de preparação antes dos projetos consumidores e declarar teardown associado.
552. [[playwright-webserver-readiness-reuse]] — A opção `webServer` inicia um processo de aplicação e aguarda a URL configurada responder antes de liberar os testes.
553. [[playwright-sharding-ci-particionamento]] — O parâmetro `--shard=x/y` seleciona uma parte da suíte, permitindo distribuir a execução entre jobs independentes.
554. [[playwright-visual-snapshots-baseline]] — `toHaveScreenshot()` compara uma captura atual com uma imagem de referência gerada e versionada para aquele teste.
555. [[playwright-page-object-contract]] — Um Page Object encapsula seletores e ações recorrentes de uma parte da aplicação, expondo aos testes uma interface de maior nível.
556. [[playwright-download-save-context]] — O evento de download fornece um objeto temporário cujo arquivo é removido quando o browser context que o criou é encerrado.
557. [[playwright-apirequest-cookie-context]] — O `APIRequestContext` ligado ao browser context usa o mesmo jar de cookies; uma instância criada isoladamente mantém armazenamento próprio.
558. [[playwright-test-step-relatorio]] — `test.step()` agrupa uma parte assíncrona do teste sob um nome que aparece como etapa da execução.
559. [[playwright-reporter-saida-por-ambiente]] — O runner inclui reporters com níveis de detalhe distintos e permite configurar mais de um para a mesma execução.
### Hypothesis — construção de estratégias, replay e configuração

560. [[hypothesis-strategy-combinators]] — Combinadores transformam ou encadeiam estratégias sem precisar reescrever o gerador e sua lógica de redução.
561. [[hyp-composite-dependent-strategies]] — `@composite` permite combinar draws de estratégias em um gerador reutilizável cuja saída depende dos valores já sorteados.
562. [[hyp-data-draw-dinamico]] — `st.data()` fornece ao teste uma interface para sortear valores adicionais durante a execução a partir de estratégias escolhidas pelo próprio caso gerado.
563. [[hyp-builds-from-type-infer]] — `builds()` pode criar instâncias de uma classe chamando seu construtor e, quando autorizado, inferindo estratégias a partir de anotações de tipo.
564. [[hyp-valid-collections-cardinality]] — Estratégias de listas, conjuntos e dicionários permitem declarar cardinalidade e tipo dos elementos diretamente no domínio gerado.
565. [[hyp-floats-dominio-na-infinito]] — Estratégias de ponto flutuante podem incluir valores especiais como NaN e infinito, além de valores finitos próximos aos limites declarados.
566. [[hyp-example-regressao-explicito]] — `@example` acrescenta uma entrada escolhida manualmente à execução de um teste baseado em propriedades.
567. [[hyp-example-database-replay]] — O banco de exemplos guarda entradas que Hypothesis encontrou e pode reutilizá-las em execuções posteriores da mesma configuração.
568. [[hyp-settings-profiles-healthchecks]] — Perfis de `settings` agrupam escolhas como orçamento de exemplos e comportamento de deadlines para ambientes com necessidades distintas.
569. [[hyp-deadline-tempo-execucao]] — O `deadline` limita quanto cada exemplo gerado pode gastar em execução, separando lentidão localizada de um teste que simplesmente consome o orçamento total da suíte.
### TestNG — dados, configuração, dependências e execução

570. [[testng-dataprovider-casos]] — `@DataProvider` associa conjuntos de argumentos a uma função `@Test`, e cada linha retornada precisa ser atribuível aos parâmetros daquele método.
571. [[testng-parameters-escopo-xml]] — `@Parameters` injeta valores declarados no `testng.xml` em métodos de teste ou de configuração que declaram os nomes correspondentes.
572. [[testng-dependencies-hard-soft]] — `dependsOnMethods` ou `dependsOnGroups` expressam pré-requisitos de execução e podem fazer o framework pular um consumidor quando uma dependência falha.
573. [[testng-groups-selecao]] — Groups etiquetam métodos ou classes e podem ser incluídos ou excluídos em configuração XML ou na linha de comando.
574. [[testng-lifecycle-heranca-hooks]] — Os métodos `@Before...` e `@After...` descrevem fases diferentes do ciclo de vida e são herdados por classes de teste.
575. [[testng-dataprovider-parallel]] — Um `DataProvider` pode pedir ao TestNG que execute em paralelo os testes gerados por suas linhas de dados.
576. [[testng-suite-parallel-threadcount]] — A suite TestNG configura se métodos, classes, testes ou instâncias são executados em paralelo e quantas threads podem ser usadas.
577. [[testng-factory-instancias]] — `@Factory` retorna objetos que o TestNG trata como instâncias de classes de teste, enquanto `@DataProvider` fornece argumentos para métodos.
578. [[testng-listener-eventos-relatorio]] — Listeners recebem eventos ou oportunidades de extensão durante a execução e podem ser registrados por anotação ou configuração da suite.
579. [[testng-invocationcount-timeout]] — `invocationCount` repete um método de teste e `invocationTimeOut` limita o tempo acumulado dessas invocações quando a contagem está definida.
### Go testing — subtestes, concorrência, fuzzing e benchmarks

580. [[go-subtests-run-filter]] — `t.Run` cria um subteste nomeado associado ao teste pai e possibilita executar subconjuntos por expressão de seleção.
581. [[go-t-cleanup-subtest-scope]] — `T.Cleanup` registra uma função que roda quando o teste e seus subtestes concluírem, respeitando ordem inversa de registro.
582. [[go-testing-helper-error-location]] — `T.Helper` marca uma função auxiliar de teste para que diagnósticos de `Error` ou `Fatal` apontem ao chamador relevante.
583. [[go-parallel-subtests-barreira]] — Um subteste que chama `t.Parallel` pausa até a função do teste pai retornar, e o pai aguarda a conclusão dos filhos paralelos.
584. [[go-fuzz-corpus-regressao]] — Um fuzz test pode combinar sementes declaradas no código com arquivos de corpus, e entradas que revelam falhas podem ser salvas para reprodução.
585. [[go-race-dinamico-limites]] — O detector de corridas instrumenta o programa e reporta acessos concorrentes incompatíveis que aconteceram durante a execução observada.
586. [[go-testing-synctest-tempo-virtual]] — `testing/synctest` executa código concorrente em uma bolha isolada com tempo virtual para testes que dependem de timers e goroutines.
587. [[go-testmain-recursos-pacote]] — `TestMain(m *testing.M)` dá ao pacote um ponto único para preparar recursos antes de rodar seus testes e limpar depois.
588. [[go-tdir-cleanup-descendants]] — `T.TempDir` cria um diretório temporário exclusivo para o teste e o remove quando o teste e seus descendentes terminam.
589. [[go-b-loop-benchmark-comparacao]] — `B.Loop` fornece uma forma atual de escrever o corpo repetido de um benchmark sem controlar manualmente `b.N`.
### PIT — mutation testing para Java

590. [[pit-mutacao-bytecode-mutantes]] — PIT aplica mutadores ao bytecode compilado para criar versões pequenas do programa que representam falhas hipotéticas.
591. [[pit-cobertura-selecao-testes]] — Antes de executar casos contra mutantes, PIT mede cobertura de linha e tempos para selecionar testes que alcançam a área modificada.
592. [[pit-status-killed-survived]] — PIT classifica resultados como `Killed`, `Survived`, `No coverage`, `Non viable` e `Timed Out`, entre outros estados documentados.
593. [[pit-mutator-groups-esforco]] — PIT oferece grupos de mutadores com alcances diferentes, incluindo `DEFAULTS`, `STRONGER` e `ALL`.
594. [[pit-targetclasses-targettests]] — `targetClasses` e `targetTests` definem, respectivamente, quais classes podem receber mutações e quais testes podem participar da análise.
595. [[pit-timeouts-mutantes-hang]] — PIT usa limite temporal para evitar que um mutante que provoque loop ou execução longa bloqueie indefinidamente a análise.
596. [[pit-incremental-history-assumptions]] — A análise incremental conserva resultados anteriores e evita recomputar mutações que PIT considera inferíveis a partir de código e testes não alterados.
597. [[pit-maven-dry-run-setup]] — O modo dry run, documentado desde PIT 1.17.3, reúne cobertura e gera mutantes sem executar a suíte contra cada mutação.
598. [[pit-maven-goal-relatorio]] — O plugin Maven expõe o goal `mutationCoverage`, que compila e executa a análise conforme os filtros definidos no projeto.
599. [[pit-mutation-score-interpretacao]] — Mutation score resume proporções de estados dos mutantes, mas não descreve quais requisitos foram testados nem o custo de interpretar sobreviventes.
### PHPUnit — descoberta, dados, fixtures e execução

600. [[phpunit-discovery-metodos-atributos]] — PHPUnit descobre métodos públicos com prefixo `test` ou métodos marcados com o atributo `#[Test]`.
601. [[phpunit-dataprovider-contrato]] — Um data provider associa conjuntos de argumentos a um método de teste e faz cada conjunto aparecer como uma execução identificável.
602. [[phpunit-testwith-inline-cases]] — O atributo `#[TestWith]` permite associar dados inline ao teste, enquanto `#[DataProvider]` mantém datasets maiores em um método nomeado.
603. [[phpunit-depends-retorno]] — `#[Depends]` declara que um teste consome o valor retornado por outro teste, mas não define sozinho a ordem de execução dos métodos.
604. [[phpunit-fixtures-per-test]] — O PHPUnit cria uma instância da classe de teste por método; `setUp()` e `tearDown()` rodam em cada caso, enquanto `setUpBeforeClass()` e `tearDownAfterClass()` cobrem o ciclo da classe.
605. [[phpunit-config-precedencia]] — A configuração efetiva é construída dos defaults internos, depois do XML e por fim das opções de CLI.
606. [[phpunit-selection-filter-group]] — O runner oferece opções para selecionar suite, grupo ou padrão de nome sem precisar editar a descoberta da classe.
607. [[phpunit-random-seed-repro]] — A opção `--order-by random` executa testes em ordem pseudoaleatória e aceita uma seed para repetir a mesma sequência.
608. [[phpunit-risky-output-assertions]] — PHPUnit pode classificar como arriscados testes sem assertions úteis ou que produzem saída, conforme verificações habilitadas.
609. [[phpunit-size-time-budget]] — Atributos Small, Medium e Large classificam testes por custo e permitem aplicar limites temporais correspondentes na configuração.
### RSpec — exemplos compartilhados, hooks, matchers e seleção

610. [[rspec-shared-examples-contrato]] — Shared examples guardam comportamentos que podem ser executados no contexto de diferentes example groups.
611. [[rspec-include-vs-it-behaves-like]] — `include_examples` inclui o conteúdo no contexto corrente, enquanto `it_behaves_like` cria um grupo aninhado para o comportamento compartilhado.
612. [[rspec-around-hook-envelope]] — Um hook `around(:example)` recebe o objeto de exemplo e envolve a execução que ocorre em `example.run`.
613. [[rspec-before-after-scope]] — Hooks `before` e `after` podem ser definidos para exemplos ou grupos e participam de uma ordem que depende do escopo.
614. [[rspec-composable-matchers-estruturas]] — Matchers compostos permitem descrever partes importantes de uma estrutura aninhada sem exigir que todo valor coincida literalmente.
615. [[rspec-verifying-doubles-interface]] — Verifying doubles checam se métodos configurados existem na classe ou objeto representado, reduzindo divergências entre mock e implementação.
616. [[rspec-message-argument-constraints]] — `with` limita quais argumentos satisfazem uma expectativa ou resposta configurada para uma mensagem recebida por double.
617. [[rspec-metadata-tag-selection]] — Metadata é associada a example groups e exemplos e pode selecionar quais casos entram numa execução da CLI.
618. [[rspec-random-order-seed]] — RSpec pode embaralhar grupos e exemplos usando uma seed que permite repetir a ordem de uma execução.
619. [[rspec-let-let-bang-lazy]] — `let` memoiza um helper quando ele é acessado pela primeira vez em cada exemplo, enquanto `let!` também agenda sua avaliação por um hook antes do exemplo.
### ExUnit — callbacks, concorrência, templates e doctests

620. [[exunit-setup-context-data]] — Callbacks `setup` podem receber contexto e retornar novos valores que são mesclados ao contexto disponível para etapas seguintes e para o teste.
621. [[exunit-setup-all-process-boundary]] — `setup_all` roda uma vez por módulo antes dos testes, em processo separado do processo de cada teste.
622. [[exunit-start-supervised-lifecycle]] — `start_supervised` inicia um processo sob supervisor vinculado ao ciclo de vida do teste e assegura seu encerramento antes de `on_exit`.
623. [[exunit-on-exit-separar-cleanup]] — Callbacks `on_exit` são executados após a saída do processo de teste e rodam em processo separado.
624. [[exunit-async-global-state]] — Com `async: true`, casos de teste podem executar em paralelo com outros módulos, enquanto testes do mesmo módulo permanecem seriais.
625. [[exunit-case-template-reuso]] — `ExUnit.CaseTemplate` permite que módulos de teste usem um template com callbacks e funções comuns.
626. [[exunit-capture-io-isolamento]] — `capture_io` substitui o group leader do processo atual durante a função e devolve o texto capturado.
627. [[exunit-doctest-documentacao]] — `doctest` extrai exemplos formatados na documentação de um módulo e os executa como verificações de comportamento.
628. [[exunit-tags-select-filters]] — Tags associadas a casos ou grupos adicionam metadata ao contexto e podem ser incluídas ou excluídas pela configuração do ExUnit.
629. [[exunit-seed-cases-concorrencia]] — ExUnit permite configurar seed para randomizar testes e `max_cases` para limitar quantos casos de módulos distintos rodam simultaneamente.
### Newman — execução de collections Postman em CLI e CI

630. [[newman-maintenance-workflow-choice]] — O README atual informa que Newman está em modo de manutenção e recomenda Postman CLI para workflows novos que precisem acompanhar recursos recentes.
631. [[newman-collection-source-version]] — `newman run` aceita uma collection exportada em arquivo JSON ou uma URL que forneça a definição da coleção.
632. [[newman-environment-global-precedence]] — O CLI recebe arquivos de environment e globals, e variáveis globais têm precedência inferior às variáveis do environment com o mesmo nome.
633. [[newman-iteration-data-csv-json]] — `--iteration-data` fornece arquivo JSON ou CSV às iterações de uma collection, e `--iteration-count` define a quantidade de execuções quando usado com esses dados.
634. [[newman-folder-selection]] — A opção `--folder` seleciona requests dentro de uma ou mais pastas ou requests nomeadas da collection.
635. [[newman-bail-exit-status]] — `--bail` pode interromper a execução ao encontrar erro em script de teste, e `--suppress-exit-code` substitui o código padrão do runner.
636. [[newman-timeout-scopes]] — Newman configura limites distintos para duração da execução, requests e scripts, que protegem partes diferentes do workflow.
637. [[newman-reporters-artifacts]] — Reporters integrados podem gerar saída terminal, JSON ou JUnit, e selecionar reporters de arquivo pode alterar se o reporter CLI continua habilitado.
638. [[newman-custom-reporter-package]] — Newman pode carregar reporters externos instalados como módulos Node compatíveis com a convenção de reporter.
639. [[newman-programmatic-events-summary]] — A API programática expõe `newman.run`, callback e eventos para iniciar collections de dentro de uma aplicação Node.
### axe-core — escopo de varredura, resultados e limites

640. [[axe-rendered-dom-state]] — axe.run analisa conteúdo renderizado no documento e não avalia automaticamente regiões ocultas que ainda não foram ativadas.
641. [[axe-context-include-exclude]] — O argumento `context` aceita seletores ou nós DOM para incluir regiões e uma configuração de exclusão para omitir áreas escolhidas.
642. [[axe-frames-shadow-dom-context]] — axe-core tem opções de contexto para limitar seleção dentro de frames e de regiões de shadow DOM.
643. [[axe-runonly-tags-rules]] — A opção `runOnly` restringe quais regras ou grupos identificados por tags participam de uma execução.
644. [[axe-result-categories]] — O objeto de resultados separa regras que falharam, passaram, exigem revisão incompleta ou não se aplicam à árvore examinada.
645. [[axe-incomplete-manual-review]] — Uma regra que não consegue decidir automaticamente pode aparecer em `incomplete` com nós que demandam avaliação adicional.
646. [[axe-impact-priorizacao-nao-conformidade]] — O campo `impact` ajuda a ordenar a severidade estimada de uma violação retornada, mas não é certificado de conformidade ou medida completa de impacto ao usuário.
647. [[axe-tags-nao-cobertura-total-wcag]] — Tags de regras identificam relação com versões ou níveis de padrões e também podem marcar melhores práticas, entre outros metadados.
648. [[axe-dynamic-flows-multiple-scans]] — Uma página interativa pode revelar conteúdo novo após abrir modal, menu ou erro de formulário, e cada estado exige uma execução própria para ser observado.
649. [[axe-result-targets-regression]] — Resultados associam violações a nós e alvos, permitindo identificar onde uma regra encontrou o problema na árvore analisada.

## Tranche 13 — frameworks de teste, Rust e execução de suites (IDs 650–749; revisão factual por IA registrada)

### Mocha — interfaces, hooks e execução paralela

650. [[mocha-bdd-suite-tree]] — A interface BDD registra grupos com `describe()` e exemplos individuais com `it()`.
651. [[mocha-hooks-nested-order]] — `before` e `after` envolvem uma suite, enquanto `beforeEach` e `afterEach` acompanham cada teste daquele escopo.
652. [[mocha-async-completion-contract]] — Mocha reconhece teste síncrono, callback `done`, promessa retornada e função `async` que devolve promessa.
653. [[mocha-root-hooks-plugin]] — Um Root Hook Plugin exporta hooks que o Mocha instala fora de uma suite nomeada.
654. [[mocha-parallel-order-isolation]] — Com `--parallel`, Mocha distribui arquivos por workers e não garante a ordem em que eles serão executados.
655. [[mocha-retry-diagnostic]] — A opção `--retries` repete testes que falham até o limite configurado; por padrão, falhas não são repetidas.
656. [[mocha-timeout-test-and-hook]] — Mocha aplica limite de duração a testes e hooks, e o valor pode ser configurado em níveis diferentes.
657. [[mocha-grep-focused-suite]] — `--grep` seleciona testes pelos títulos correspondentes e pode ser usado para executar um recorte sem alterar a suíte.
658. [[mocha-reporter-parallel-output]] — Reporters transformam resultados em saída de terminal ou arquivos, e algumas opções precisam conhecer a suíte inteira antes da execução.
659. [[mocha-global-fixture-lifecycle]] — Global fixtures oferecem configuração e limpeza uma vez para a execução do Mocha, ao passo que hooks pertencem às suites e seus testes.

### Jasmine 7 — spies, relógio simulado e execução assíncrona

660. [[jasmine-promise-completion]] — Jasmine aguarda a promessa retornada por um spec ou hook e falha o spec quando ela rejeita.
661. [[jasmine-done-callback]] — Ao declarar argumento `done`, o spec ou hook usa o callback entregue por Jasmine para sinalizar conclusão.
662. [[jasmine-clock-tick-cleanup]] — `jasmine.clock()` instala relógio simulado que permite avançar timers enfileirados sem esperar tempo real.
663. [[jasmine-mock-date-time]] — O relógio de Jasmine pode ser instruído a simular a data que `new Date()` retorna.
664. [[jasmine-spy-through-vs-stub]] — Um spy pode registrar chamadas e também ser configurado para executar a implementação original ou devolver comportamento falso.
665. [[jasmine-spy-call-history]] — O objeto Spy expõe histórico de chamadas para examinar quantidade, argumentos e ordem observada.
666. [[jasmine-beforeall-state-boundary]] — `beforeAll` prepara uma vez os specs de seu grupo, enquanto `beforeEach` roda antes de cada spec.
667. [[jasmine-focused-spec-cleanup]] — `fit` e `fdescribe` focam uma spec ou suite e fazem com que apenas testes focados sejam executados.
668. [[jasmine-pending-spec-intent]] — Um spec `it` sem função de teste é marcado como pending, e a API também distingue specs focados.
669. [[jasmine-async-matcher-await]] — `expectAsync()` cria expectations cujos matchers retornam promises que precisam ser aguardadas ou retornadas.

### WebdriverIO — espera explícita, runners e isolamento

670. [[webdriverio-auto-wait-interactable]] — Comandos que interagem diretamente com elemento aguardam que ele esteja visível e interagível antes de agir.
671. [[webdriverio-waituntil-condition]] — `browser.waitUntil()` consulta uma condição até que ela retorne valor truthy ou ultrapasse o timeout configurado.
672. [[webdriverio-wait-displayed-state]] — `waitForDisplayed()` aguarda que um elemento esteja exibido, condição diferente de apenas localizar um seletor no DOM.
673. [[webdriverio-soft-assertion-aggregation]] — `expect.soft()` coleta falhas sem interromper imediatamente o teste e as reporta juntas ao final quando o serviço correspondente está ativo.
674. [[webdriverio-local-worker-isolation]] — No Local Runner, cada arquivo de teste roda em processo worker separado por capability, com sua própria sessão de browser.
675. [[webdriverio-browser-runner-boundary]] — Browser Runner executa framework de teste dentro de browser real e é diferente do Local Runner que inicia framework em processo Node.
676. [[webdriverio-selector-contract]] — WebdriverIO aceita estratégias de seletor diferentes, que variam em estabilidade e relação com a interface de usuário.
677. [[webdriverio-capability-concurrency]] — Configuração do runner combina capabilities de browser e limites de execução concorrente.
678. [[webdriverio-spec-file-retries]] — Configuração pode repetir um arquivo de spec que falhou até o limite `specFileRetries`.
679. [[webdriverio-group-spec-execution]] — Suite pode ser organizada em grupos de spec que executam juntos, útil quando uma dependência de execução é inevitável.

### Cargo test e rustdoc — organização e controle de execução

680. [[cargo-unit-test-module]] — Unit tests escritos num módulo `#[cfg(test)]` dentro do arquivo podem acessar itens privados do módulo pai.
681. [[cargo-integration-test-crate]] — Arquivos no diretório superior `tests/` são compilados individualmente como crates de integração.
682. [[rustdoc-compile-fail-doctest]] — A cerca `compile_fail` marca um bloco de documentação que rustdoc compila negativamente e aprova quando o trecho não compila.
683. [[cargo-doctest-hidden-setup]] — Linhas iniciadas por `#` podem compor contexto compilável do doctest sem aparecer no trecho renderizado.
684. [[cargo-test-filter-argument-boundary]] — O argumento de filtro e os parâmetros depois de `--` são encaminhados ao executável de teste, enquanto opções antes do separador pertencem ao Cargo.
685. [[cargo-no-run-compilation-check]] — A opção `--no-run` compila executáveis de teste sem iniciar o harness.
686. [[cargo-no-fail-fast-scope]] — `--no-fail-fast` faz Cargo continuar para executáveis de teste posteriores depois de um deles falhar.
687. [[cargo-test-thread-count-isolation]] — Testes do harness podem rodar em múltiplas threads, e `--test-threads` limita a concorrência desse executável.
688. [[cargo-target-selection]] — Cargo consegue selecionar workspace, pacote, biblioteca, binário, exemplo ou alvo de integração em vez de compilar tudo.
689. [[cargo-harness-false-boundary]] — Alvos com `harness = false` deixam de receber o harness automático e precisam fornecer seu próprio `main` para executar testes.

### Criterion.rs — metodologia, configuração e interpretação de benchmarks

690. [[criterion-benchmark-input-black-box]] — `bench_with_input()` associa um valor de entrada e um identificador ao benchmark e passa o input por `black_box`.
691. [[criterion-benchmark-group-parameters]] — `BenchmarkGroup` relaciona casos que medem a mesma pergunta com parâmetros diferentes e gera sumarização conjunta.
692. [[criterion-throughput-units]] — Throughput em bytes ou elementos exige informar quantos deles são processados em cada iteração.
693. [[criterion-warmup-measurement-phases]] — Execução de benchmark passa por warmup, medição, análise e comparação com resultados salvos.
694. [[criterion-sample-size-tradeoff]] — A quantidade de amostras afeta duração da execução e capacidade de estimar diferenças pequenas com a análise estatística configurada.
695. [[criterion-outlier-interpretation]] — Criterion classifica outliers e avisa sobre sua presença, mas a análise subsequente continua usando as amostras coletadas.
696. [[criterion-baseline-comparison]] — Criterion compara estatísticas atuais com dados previamente salvos e estima se a diferença pode ser atribuída a variação.
697. [[criterion-flat-sampling-long-workload]] — Criterion oferece modos de amostragem `Auto`, `Linear` e `Flat`, sendo o último destinado a benchmarks de longa duração.
698. [[criterion-throughput-and-log-scale]] — Grupos podem descrever throughput e usar escala logarítmica quando tamanhos de input crescem exponencialmente.
699. [[criterion-benchmark-loop-scope]] — A closure de benchmark precisa repetir o trabalho que se deseja medir e evitar que preparação não representativa domine a duração.

### Ginkgo v2 — árvore de specs, paralelismo e confiabilidade

700. [[ginkgo-container-tree]] — Ginkgo usa `Describe`, `Context` e `It` para compor uma árvore de especificações que o runner constrói antes de executar os casos.
701. [[ginkgo-before-after-nesting]] — `BeforeEach` roda para cada spec em seu escopo e hooks aninhados seguem hierarquia do container.
702. [[ginkgo-suite-synchronized-setup]] — Suite-level setup e teardown têm nós próprios; em execução paralela, recurso compartilhado exige coordenação entre processos.
703. [[ginkgo-process-parallel-isolation]] — CLI `ginkgo -p` executa specs usando processos paralelos e acelera suites que não compartilham recurso mutável.
704. [[ginkgo-random-order-seed]] — Randomização muda ordem de execução dos specs e seed permite repetir a sequência que revelou dependência entre casos.
705. [[ginkgo-label-filter]] — Labels associam metadados a specs e filtros permitem selecionar conjuntos sem comentar ou editar a árvore de testes.
706. [[ginkgo-describe-table-entries]] — `DescribeTable` e `Entry` produzem specs a partir de exemplos declarados de forma explícita.
707. [[ginkgo-eventually-context]] — `Eventually` repete observação até matcher passar ou contexto/timeout encerrar a tentativa.
708. [[ginkgo-consistently-window]] — `Consistently` avalia matcher por uma janela temporal para verificar que condição permanece verdadeira ou comportamento indesejado não aparece.
709. [[ginkgo-flake-attempts-evidence]] — `FlakeAttempts` permite executar novamente um spec marcado como flakey até o limite definido.

### ScalaTest 3.2 — estilos, fixtures, tags e tabelas

710. [[scalatest-style-selection]] — ScalaTest oferece style traits que adaptam a forma de declarar testes sem mudar o conceito central de `Suite`.
711. [[scalatest-pending-cancel-semantics]] — Pending indica teste conhecido que ainda não foi implementado, enquanto cancel interrompe execução por condição que impede avaliação naquele contexto.
712. [[scalatest-assertion-clue]] — Assertions ScalaTest podem carregar pistas contextuais para indicar qual etapa ou dado contribuiu para uma falha.
713. [[scalatest-tags-select-test-runs]] — Tags classificam testes e runners permitem incluir ou excluir grupos durante a execução.
714. [[scalatest-runner-entrypoints]] — ScalaTest pode ser executado por frameworks de build, Runner de linha de comando, IDEs e integrações específicas.
715. [[scalatest-fixture-withfixture]] — `withFixture` permite envolver execução de testes com preparação e cleanup comuns a grande parte de uma suite.
716. [[scalatest-loan-fixture-cleanup]] — Loan-fixture é opção quando testes diferentes precisam de objetos específicos que precisam ser limpos ao concluir.
717. [[scalatest-table-driven-check]] — `TableDrivenPropertyChecks` aplica uma propriedade às linhas tipadas de `Table` usando métodos como `forAll` e `forEvery`.
718. [[scalatest-matcher-composition]] — Matchers fornecem linguagem declarativa para comparar estado observado com condição esperada.
719. [[scalatest-async-future-result]] — Estilos assíncronos do ScalaTest integram resultado de teste com `Future` e só concluem quando esse resultado finaliza.

### Spock 2.4 — fixtures, dados e interações

720. [[spock-given-when-then-contract]] — Uma feature Spock pode separar preparação, estímulo e resultado nos blocos `given:`, `when:` e `then:`.
721. [[spock-fixture-lifecycle-order]] — `setupSpec`, `setup`, `cleanup` e `cleanupSpec` cobrem preparação e liberação em escopos diferentes.
722. [[spock-shared-field-scope]] — Campos de instância recebem objeto independente para cada feature; `@Shared` amplia vida útil e partilha objeto entre métodos.
723. [[spock-data-table-iterations]] — Bloco `where:` fornece data variables que executam a mesma feature para cada linha da tabela.
724. [[spock-where-iteration-isolation]] — Cada iteração de feature data-driven ganha instância própria da specification e passa por setup e cleanup.
725. [[spock-mock-interaction-constraints]] — Interação em bloco `then:` descreve chamadas esperadas por cardinalidade, alvo, método e argumentos.
726. [[spock-stub-response-generator]] — Operador `>>` define resposta que mock ou stub fornece quando recebe chamada correspondente.
727. [[spock-lenient-mock-scope]] — Mocks Spock são lenientes por padrão para chamadas inesperadas que não foram descritas, respondendo com valor default.
728. [[spock-exception-condition]] — Condições de Spock ajudam verificar comportamento de exceção no caminho em que ela é lançada.
729. [[spock-extension-boundary]] — Extensions registram comportamento reaproveitável que intercepta ou complementa lifecycle de specs e features.

### GoogleTest — fixtures, parametrização, assertions e gMock

730. [[googletest-test-suite-registration]] — Macro `TEST()` registra função de teste associada a uma suite nomeada, sem exigir lista manual para executar os casos.
731. [[googletest-test-fixture-instance]] — `TEST_F` liga caso a uma classe derivada de `testing::Test`, e cada teste usa objeto fixture próprio.
732. [[googletest-fatal-vs-nonfatal]] — `ASSERT_*` interrompe a função de teste no primeiro erro, enquanto `EXPECT_*` registra falha não fatal e continua.
733. [[googletest-value-parameterized-suite]] — Teste value-parameterized reutiliza um padrão de fixture e executa para valores fornecidos por gerador.
734. [[googletest-typed-test-known-types]] — Typed tests executam o mesmo conjunto de definições para uma lista de tipos conhecida na compilação.
735. [[googletest-type-parameterized-contract]] — Type-parameterized tests definem padrões antes de conhecer a lista concreta de tipos que os instanciará.
736. [[googletest-filter-selected-tests]] — Filtro `--gtest_filter` seleciona suites e testes pelo padrão de nome durante execução.
737. [[googletest-death-test-process]] — Death tests verificam se uma operação encerra ou termina processo segundo condição esperada.
738. [[googletest-global-environment-boundary]] — Test environment oferece `SetUp` e `TearDown` de escopo do programa, diferente de fixture por teste.
739. [[gmock-interaction-expectation]] — `EXPECT_CALL` descreve chamada esperada a mock, incluindo método, argumentos, frequência e resposta opcional.

### CTest e CMake — descoberta, fixtures, filtros e relatórios

740. [[ctest-enable-testing-scope]] — CTest executa testes descritos em `CTestTestfile.cmake`, que CMake gera quando testing foi habilitado no diretório apropriado.
741. [[ctest-add-test-command]] — A assinatura nomeada de `add_test(NAME ... COMMAND ...)` associa identificador estável e comando ao teste executado por CTest.
742. [[ctest-working-directory-contract]] — `WORKING_DIRECTORY` define o diretório de execução do teste; quando omitido, CTest usa diretório binário atual.
743. [[ctest-exit-code-will-fail]] — Por padrão, código de saída zero aprova teste e código diferente de zero o reprova; `WILL_FAIL` inverte essa lógica para casos que esperam retorno de falha.
744. [[ctest-timeout-failure-diagnostic]] — Propriedade TIMEOUT define limite de parede por teste e impede processo travado de bloquear indefinidamente a suite.
745. [[ctest-label-filter]] — Propriedade `LABELS` classifica teste e CTest permite selecionar ou excluir rótulos sem renomear alvo.
746. [[ctest-fixture-dependency-graph]] — `FIXTURES_SETUP` marca um teste preparatório e `FIXTURES_REQUIRED` marca consumidores que precisam daquele recurso.
747. [[ctest-parallel-processors]] — CTest pode executar testes em paralelo, e propriedade PROCESSORS informa quantos slots cada caso consome.
748. [[ctest-repeat-and-random-order]] — CTest oferece opções de repetição e ordem aleatória para exercitar casos várias vezes no mesmo run.
749. [[ctest-junit-preset-output]] — Test Preset guarda opções de execução reutilizáveis e CTest pode gravar saída JUnit com `--output-junit`.

## Tranche 14 — frameworks de build, teste e tooling atuais

### Bazel — testes herméticos, sinais de execução e resultados

750. [[bazel-test-hermetic-runtime-boundary]] — Um teste executado por Bazel deve depender de fontes declaradas, produtos de build declarados e recursos cujo comportamento o runner garante.
751. [[bazel-test-runtime-files-through-runfiles]] — Arquivos usados durante a execução devem chegar ao teste como entradas de runtime do alvo, e não por caminhos presumidos na árvore de saída.
752. [[bazel-test-shard-contract]] — `shard_count` solicita shards, mas cabe ao test runner suportar a partição e usar os índices de shard que o Bazel fornece.
753. [[bazel-test-size-and-timeout]] — `size` informa a demanda de recursos presumida, enquanto `timeout` define a classe de duração; os atributos são relacionados, mas não intercambiáveis.
754. [[bazel-test-output-as-diagnostic-policy]] — `--test_output` controla como stdout e stderr dos testes aparecem durante `bazel test`, com modos úteis para resumo, falhas, tudo ou transmissão ao vivo.
755. [[bazel-test-env-declaration]] — `--test_env` injeta uma variável no ambiente do teste; especificar valor fixa esse valor, enquanto omiti-lo herda o valor do shell que iniciou Bazel.
756. [[bazel-test-arg-forwarding]] — `--test_arg` encaminha argumentos ao programa de teste, permitindo usar filtros próprios sem confundir opções do framework com flags de Bazel.
757. [[bazel-test-target-selection-patterns]] — `bazel test` seleciona regras de teste por labels e padrões de targets, não por nomes internos de métodos de qualquer framework.
758. [[bazel-build-event-protocol-test-results]] — Build Event Protocol representa a invocação como eventos estruturados e inclui resultados e progresso de testes para ferramentas consumidoras.
759. [[bazel-remote-test-environment]] — Execução remota distribui ações de build e teste em workers, portanto o teste não deve depender de estado local não declarado.

### Maven Surefire e Failsafe — ciclo de vida, seleção e isolamento

760. [[maven-surefire-test-phase]] — Surefire executa testes unitários na fase `test` do ciclo Maven e produz relatórios texto e XML no diretório padrão do projeto.
761. [[maven-failsafe-verify-lifecycle]] — Failsafe separa execução de testes de integração em `integration-test` da avaliação final de resultados em `verify`.
762. [[maven-single-test-selection]] — A propriedade `-Dtest` seleciona classes ou métodos para Surefire, e deve ser tratada como filtro de diagnóstico, não como execução integral.
763. [[maven-junit-platform-provider-boundary]] — A integração com JUnit Platform usa engines presentes nas dependências para executar frameworks compatíveis; no Surefire 3.6.0 o provider unificado é documentado.
764. [[maven-test-class-naming-patterns]] — Os padrões de inclusão do Surefire determinam quais classes compiladas entram na execução padrão.
765. [[maven-fork-count-process-isolation]] — `forkCount` limita quantas JVMs de teste são abertas em paralelo; valor zero executa no processo Maven, enquanto valor positivo usa processos separados.
766. [[maven-parallel-tests-thread-safety]] — Surefire não executa testes em paralelo por padrão; paralelismo precisa ser configurado segundo provider e estrutura de testes.
767. [[maven-skip-execution-vs-test-compilation]] — `-DskipTests` pula a execução dos testes, enquanto `-Dmaven.test.skip=true` também pode pular a compilação do código de teste.
768. [[maven-rerun-flaky-evidence]] — `rerunFailingTestsCount` repete falhas até aprovação ou esgotamento e o Surefire marca um caso que passa depois de falhar como flaky.
769. [[maven-failsafe-report-separation]] — Failsafe registra resultados de integração em formato compatível com Surefire, mas seus relatórios ficam em diretório próprio.

### Gradle — tasks Test, suites JVM e isolamento de execução

770. [[gradle-test-task-input-contract]] — Uma task Gradle do tipo `Test` precisa dos diretórios de classes de teste e do classpath de execução para descobrir e executar casos JVM.
771. [[gradle-select-junit-platform-engine]] — Adicionar uma dependência de teste não basta para selecionar o mecanismo de execução; a task `Test` deve usar a plataforma apropriada ao framework.
772. [[gradle-jvm-test-suite-boundary]] — O plugin JVM Test Suite permite agrupar testes por propósito, com source, dependências, framework e task próprios.
773. [[gradle-check-dependency-for-suite]] — Uma suite de teste adicional não passa a rodar em `check` apenas por existir; seu vínculo com o lifecycle deve ser declarado.
774. [[gradle-parallel-forks-and-unique-resources]] — `maxParallelForks` define o máximo de processos de teste concorrentes e seu valor padrão é um.
775. [[gradle-fork-every-process-reset]] — `forkEvery` reinicia o processo de teste depois de certo número de classes ou definições executadas.
776. [[gradle-test-filter-vs-discovery]] — O filtro da task permite reduzir quais testes são executados, enquanto a descoberta identifica classes e métodos reconhecidos pelo framework.
777. [[gradle-fail-on-empty-test-discovery]] — `failOnNoDiscoveredTests` pode impedir que uma task com fontes de teste existentes termine silenciosamente sem descobrir nenhum teste.
778. [[gradle-test-report-artifact-contract]] — Cada task de teste produz resultados que o Gradle pode converter em relatórios, e suites separadas permitem inspecionar resultados por finalidade.
779. [[gradle-ignore-failures-policy]] — `ignoreFailures` permite que o build prossiga após falha da task Test, mas não altera o resultado individual dos testes.

### Django 6.1 — cliente, banco, views e isolamento de settings

780. [[django-testcase-database-isolation]] — `django.test.TestCase` executa cada teste com isolamento transacional e é a base adequada para a maioria dos casos que consultam ou alteram o banco.
781. [[django-client-without-live-server]] — O `django.test.Client` simula requisições à aplicação sem exigir que um servidor de desenvolvimento esteja rodando.
782. [[django-requestfactory-middleware-boundary]] — `RequestFactory` cria objetos request para passar diretamente a uma view, sem executar o ciclo de roteamento e middleware.
783. [[django-setuptestdata-class-fixture]] — `setUpTestData()` prepara dados de banco uma vez por classe `TestCase`, ao passo que `setUp()` roda antes de cada método de teste.
784. [[django-live-server-browser-boundary]] — `LiveServerTestCase` inicia um servidor de teste em thread para permitir que Selenium ou outro cliente real interaja com a aplicação.
785. [[django-assert-num-queries-scope]] — `assertNumQueries` verifica quantas queries SQL foram executadas dentro de um bloco ou por uma operação específica do teste.
786. [[django-email-outbox-testing]] — Durante testes, Django fornece uma caixa de saída em memória para observar mensagens enviadas pelo código da aplicação.
787. [[django-override-settings-scope]] — `override_settings` substitui temporariamente valores de settings e restaura o contexto ao final do escopo gerenciado.
788. [[django-test-discovery-and-labels]] — O comando `manage.py test` descobre por padrão módulos que seguem o padrão de nomes de teste e aceita labels para reduzir o escopo.
789. [[django-client-csrf-enforcement]] — O cliente Django desativa verificações CSRF por padrão, então um POST aceito pelo Client não prova sozinho que a proteção foi aplicada.

### Android Espresso — sincronização, intents, listas e acessibilidade

790. [[espresso-view-action-assertion-chain]] — O fluxo central do Espresso separa a seleção de uma view, a ação do usuário e a assertion sobre o estado apresentado.
791. [[espresso-automatic-idle-boundary]] — Espresso aguarda condições conhecidas da fila de UI e recursos de idling registrados, mas não entende automaticamente toda tarefa de background.
792. [[espresso-register-idling-resource-lifecycle]] — Os benefícios de sincronização começam quando Espresso consulta o recurso; registrar antecipadamente evita uma primeira ação que passe sem observá-lo.
793. [[espresso-intents-validate-outgoing]] — `intended()` verifica se um intent de saída que corresponde ao matcher foi registrado pelo Espresso-Intents.
794. [[espresso-intents-stub-response]] — `intending()` configura uma resposta para intents de saída correspondentes e permite testar o fluxo local sem abrir o aplicativo externo.
795. [[espresso-adapter-view-ondata-selection]] — `onData()` procura o objeto de dados que alimenta uma `AdapterView` e pode rolar a lista até tornar a linha correspondente visível.
796. [[espresso-recyclerview-actions]] — `RecyclerViewActions` oferece ações de lista para localizar e operar itens que podem não estar materializados na tela.
797. [[espresso-accessibility-checks-at-actions]] — `AccessibilityChecks.enable()` integra verificações do Android Accessibility Test Framework às ações de view feitas pelos testes Espresso.
798. [[espresso-suppress-accessibility-narrowly]] — O matcher de supressão deve identificar um finding específico, em vez de silenciar toda uma categoria ou tela.
799. [[espresso-webview-testing-boundary]] — Espresso-Web é apropriado para exercitar o WebView como parte de uma aplicação híbrida e pode ser combinado a operações Espresso em views nativas.

### Rails 8.1 — fixtures, integração HTTP, tempo, jobs e paralelismo

800. [[rails-fixtures-stable-reference-data]] — Fixtures Active Record armazenam dados de teste declarativos e permitem que casos usem um conjunto conhecido de registros.
801. [[rails-test-environment-database-boundary]] — Rails executa testes sob `RAILS_ENV=test` e configura um banco de teste distinto conforme a configuração da aplicação.
802. [[rails-integration-test-full-stack-flow]] — `ActionDispatch::IntegrationTest` exercita vários controllers e o caminho completo entre dispatcher, aplicação e banco.
803. [[rails-integration-json-response-contract]] — `IntegrationTest` permite declarar formato de request e inspecionar corpo parseado para testar um endpoint JSON dentro da aplicação.
804. [[rails-system-test-browser-scope]] — Rails system tests usam Capybara para exercitar a aplicação no browser, inclusive comportamento JavaScript percebido pelo usuário.
805. [[rails-parallel-process-test-isolation]] — Rails pode distribuir testes por processos e criar bancos de teste correspondentes a workers quando a configuração de banco está disponível.
806. [[rails-freeze-time-helper-cleanup]] — `travel_to` e `freeze_time` substituem fontes de tempo relevantes para testar vencimentos e agendamentos sem esperar pelo relógio real.
807. [[rails-activejob-enqueue-vs-perform]] — Active Job oferece helpers de teste para observar jobs enfileirados e executar jobs sob demanda com o adapter de teste.
808. [[rails-mailer-generation-and-delivery-tests]] — Rails oferece testes de mailer para verificar mensagem construída e testes de integração para o fluxo de entrega acionado por outra camada.
809. [[rails-test-file-and-line-selection]] — O comando `bin/rails test` aceita um caminho de teste e seletores mais específicos para encurtar o ciclo de investigação.

### tox 4 — ambientes reproduzíveis, fatores e execução

810. [[tox-toml-over-deprecated-ini]] — tox 4 aceita TOML nativo e mantém INI por compatibilidade, mas a documentação marca INI como obsoleto e congelado.
811. [[tox-env-list-is-default-matrix]] — `env_list` define ambientes que tox seleciona por padrão quando a execução não recebe um escopo mais restrito.
812. [[tox-factor-matrix-combinations]] — Fatores são segmentos do nome do ambiente e permitem condicionar dependências ou comandos por combinação, incluindo plataforma.
813. [[tox-deps-commands-and-posargs]] — Configuração tox define dependências de ambiente e comandos a executar, podendo encaminhar argumentos do usuário ao runner.
814. [[tox-env-selection-sequential-vs-parallel]] — `tox run -e` executa ambientes escolhidos segundo a ordem especificada, enquanto o subcomando `tox parallel` executa em modo concorrente.
815. [[tox-pass-env-explicit-contract]] — `pass_env` seleciona variáveis do ambiente do processo que podem atravessar para a execução do ambiente tox.
816. [[tox-config-command-as-debugging-tool]] — O comando `tox config` mostra valores efetivos de um ambiente, incluindo herança e substituições aplicadas.
817. [[tox-exec-is-not-configured-test-run]] — `tox exec` roda um comando pontual no ambiente selecionado, sem executar `commands`, `commands_pre` ou `commands_post`, e sem instalar pacote.
818. [[tox-parallel-pytest-temp-isolation]] — Quando tox paraleliza ambientes que executam pytest, cada invocação deve usar diretório temporário próprio para evitar colisões.
819. [[tox-package-under-test-contract]] — tox pode preparar um pacote do projeto e instalá-lo no ambiente antes de rodar os comandos configurados.

### Nox — sessões Python, parametrização e seleção de tarefas

820. [[nox-python-version-matrix]] — Uma sessão Nox pode declarar vários intérpretes e gerar uma execução isolada para cada versão suportada.
821. [[nox-parametrize-session-axis]] — `nox.parametrize` expande uma função de sessão em invocações distintas com argumentos definidos pela matriz.
822. [[nox-recreate-vs-reuse-venv]] — Por padrão, Nox recria virtualenvs a cada execução; reuso é opção consciente para acelerar ciclos locais.
823. [[nox-no-virtualenv-scope]] — `python=False` ou backend `none` executa sessão sem criar virtualenv gerenciada pelo Nox.
824. [[nox-default-session-surface]] — Por padrão Nox executa todas as sessões configuradas, a menos que opções ou `default=False` alterem a seleção padrão.
825. [[nox-requires-session-dependency-order]] — `requires` permite que uma sessão dependa de outras, cuja ordem de execução Nox resolve de forma estável e topológica.
826. [[nox-tag-filtered-ci-selection]] — Sessões Nox aceitam tags e a CLI pode filtrar sessões por tags ou expressão de keywords.
827. [[nox-session-install-run-boundary]] — `session.install()` prepara pacotes no ambiente da sessão, enquanto `session.run()` invoca comandos dentro do contexto daquela sessão.
828. [[nox-external-command-boundary]] — `session.run` espera comando disponível no ambiente da sessão; executável do host deve ser autorizado de forma explícita quando necessário.
829. [[nox-posargs-test-filter-forwarding]] — Nox expõe argumentos posicionais da sessão para que o chamador acrescente opções do test runner.

### Laravel 13 — HTTP, banco e fakes de dependências

830. [[laravel-unit-vs-feature-bootstrap]] — Testes Unit não iniciam a aplicação Laravel e por isso não acessam automaticamente banco ou serviços do framework; Feature tests podem atravessar objetos e requests HTTP.
831. [[laravel-testing-environment-boundary]] — Laravel configura ambiente de teste por meio da configuração de PHPUnit e fornece arquivo `.env.testing` para valores específicos de teste.
832. [[laravel-refresh-database-transaction-contract]] — `RefreshDatabase` limpa o estado entre testes e, se o schema já estiver atualizado, executa o teste em transação sem migrar novamente.
833. [[laravel-http-test-internal-request]] — Os métodos de HTTP tests exercitam a aplicação sem emitir uma requisição real pela rede e retornam uma resposta de teste com assertions.
834. [[laravel-json-path-assertions]] — Fluent JSON assertions permitem verificar caminho, estrutura e valores selecionados sem fixar detalhes irrelevantes do documento completo.
835. [[laravel-http-client-fake-prevent-network]] — `Http::fake` substitui respostas de saída do HTTP client Laravel e pode evitar que teste faça requests para serviços externos.
836. [[laravel-event-fake-scope]] — Fakes de eventos permitem verificar dispatch sem executar listeners reais que podem enviar notificações, chamar rede ou alterar outros sistemas.
837. [[laravel-queue-fake-job-contract]] — `Queue::fake()` permite inspecionar jobs enviados à fila sem iniciar worker nem usar o backend real.
838. [[laravel-mail-fake-content-vs-delivery]] — `Mail::fake()` registra mailables enviados para que testes verifiquem destinatário e conteúdo sem acessar transporte externo.
839. [[laravel-parallel-test-database-tokens]] — Ao executar testes em paralelo, Laravel cria e migra bancos de teste por processo usando um token único no nome.

### Python unittest — descoberta, fixtures, subtests e mocks

840. [[python-unittest-discovery-names]] — `unittest` descobre métodos pelo padrão `test` e o discovery recursivo usa convenções de nomes de arquivos e pacotes.
841. [[python-unittest-subtest-dimensions]] — `subTest()` marca uma subexecução com parâmetros durante o mesmo método e permite identificar qual combinação falhou.
842. [[python-unittest-setuptestdata-lifecycle]] — `setUp()` e `tearDown()` executam em torno de cada método de teste, enquanto setup de classe é compartilhado por métodos da mesma classe.
843. [[python-unittest-addcleanup-lifo]] — `addCleanup()` registra funções que rodam em ordem inversa de registro ao finalizar o caso, inclusive quando `setUp()` falha depois do registro.
844. [[python-unittest-assert-raises-regex]] — `assertRaisesRegex` verifica que uma chamada lança o tipo de exceção esperado e que sua mensagem combina com uma expressão regular.
845. [[python-unittest-skip-vs-expected-failure]] — Skip remove temporariamente um teste da execução com motivo; `expectedFailure` marca que o caso deve falhar e registra sucesso inesperado como resultado distinto.
846. [[python-mock-patch-lookup-namespace]] — `patch()` substitui um objeto no namespace em que o código sob teste procura o nome, não necessariamente onde a classe foi originalmente definida.
847. [[python-mock-autospec-interface-check]] — `autospec` cria mocks guiados pela assinatura ou interface do objeto real e pode rejeitar atributos que não existem.
848. [[python-isolated-asyncio-testcase-lifecycle]] — `IsolatedAsyncioTestCase` permite escrever setup, teste e teardown assíncronos mantendo o contrato de TestCase.
849. [[python-unittest-assertlogs-context]] — `assertLogs()` captura registros de logging de um logger durante um bloco e permite verificar nível e conteúdo sem interceptar stdout.

## Tranche 15 — frameworks, mocks, cobertura e automação móvel

### Puppeteer — locators, avaliação, rede, protocolos e evidências

850. [[puppeteer-locator-auto-waiting]] — Um locator representa um elemento que pode ainda não existir e só resolve sua localização quando uma ação ou condição é solicitada por meio dele.
851. [[puppeteer-page-evaluate-serialization]] — `page.evaluate()` executa uma função dentro do navegador e devolve apenas valores serializáveis para o processo Node que controla a automação.
852. [[puppeteer-selector-syntax-beyond-css]] — Além de seletores CSS, o Puppeteer aceita extensões como `::-p-text()`, `::-p-aria()` e o combinador `>>>` para atravessar shadow roots abertos.
853. [[puppeteer-network-interception-cooperative]] — Com a interceptação ativa, mais de uma callback pode opinar sobre a mesma requisição, e a resolução cooperativa decide o resultado pela prioridade informada em cada voto.
854. [[puppeteer-request-abort-and-continue]] — Cada requisição capturada precisa terminar em `continue`, `abort` ou `respond`; enquanto isso não acontece, a navegação permanece pendente aguardando a decisão.
855. [[puppeteer-bidi-vs-cdp]] — O Puppeteer controla navegadores por DevTools Protocol ou por WebDriver BiDi, com BiDi como padrão no Firefox e CDP ainda como padrão no Chrome.
856. [[puppeteer-headless-modes]] — O modo headless moderno é o padrão de lançamento, e o binário reduzido `chrome-headless-shell` é solicitado com `headless: 'shell'`, enquanto `headless: false` abre a janela para depuração.
857. [[puppeteer-navigation-race-free]] — Uma ação que dispara navegação deve ser aguardada em conjunto com a espera pelo resultado, para que o observador exista antes de o evento acontecer.
858. [[puppeteer-screenshots-artifacts]] — `page.screenshot()` grava imagem da viewport, da página inteira ou de uma região delimitada, servindo como evidência de falha e insumo de comparação visual.
859. [[puppeteer-browser-context-isolation]] — Cada contexto de navegador mantém cookies, cache e armazenamento próprios, funcionando como um perfil isolado dentro da mesma instância de navegador.

### Mock Service Worker 2 — handlers, respostas, ciclo de vida e padrões de rede

860. [[msw-setupserver-node-interception]] — `setupServer` configura a interceptação de requisições no processo Node sem abrir porta ou servidor real, aplicando os mesmos handlers usados no navegador.
861. [[msw-lifecycle-listen-reset-close]] — O ciclo recomendado inicia a interceptação antes de todos os testes, remove handlers adicionados por cada caso e encerra o servidor ao final da suíte.
862. [[msw-onunhandledrequest-fail]] — Por padrão, uma requisição sem handler correspondente gera aviso; a opção `onUnhandledRequest` permite elevá-la a erro ou fornecer tratamento próprio.
863. [[msw-handler-order-and-overrides]] — As requisições percorrem a lista de handlers em ordem até o primeiro que produzir uma instrução, e `server.use()` insere novos handlers no início da lista.
864. [[msw-passthrough-real-response]] — Retornar `passthrough()` executa a requisição original e devolve a resposta real, e ainda assim a requisição é considerada tratada para fins de resolução.
865. [[msw-httpresponse-construction]] — `HttpResponse` oferece métodos como `json`, `text`, `html` e `error` para compor status, cabeçalhos e corpo da resposta mockada de forma tipada.
866. [[msw-url-patterns-and-params]] — Padrões de URL podem incluir parâmetros de caminho como `:id`, curingas e expressões, e o resolver recebe os valores extraídos para montar a resposta.
867. [[msw-async-handler-and-body]] — Ler o corpo com `await request.json()` exige um resolver assíncrono; um resolver síncrono que tenta aguardar o corpo devolve resultado indefinido.
868. [[msw-shared-handlers-across-environments]] — A mesma lista de handlers pode atender testes automatizados, desenvolvimento local e catálogo de componentes, mantendo uma única descrição do comportamento simulado.
869. [[msw-per-test-error-overrides]] — Um teste específico pode registrar handlers de falha com `server.use()`, substituindo temporariamente o caminho feliz sem alterar a definição global.

### Supertest — requisições HTTP, agentes, asserções e ciclo do servidor

870. [[supertest-agent-persistent-cookies]] — `request.agent(app)` mantém os cookies recebidos entre chamadas, reproduzindo o comportamento de um cliente que preserva sessão entre requisições.
871. [[supertest-chained-expectations]] — O método `expect` permite afirmar status, cabeçalhos e corpo em uma única cadeia encadeada à requisição, com falha apontando a expectativa violada.
872. [[supertest-send-json-body]] — Chamar `.send()` com um objeto faz o Superagent serializar o conteúdo como JSON e definir o cabeçalho de tipo de conteúdo correspondente.
873. [[supertest-end-callback-error-handling]] — O método `end` recebe callback com erro e resposta e pode ser usado quando o teste precisa de controle explícito, enquanto o estilo de promessa cobre a maioria dos casos.
874. [[supertest-multipart-attach]] — O método `attach` adiciona uma parte de arquivo a uma requisição multipart, recebendo caminho do documento e campos adicionais do formulário.
875. [[supertest-auth-headers-set]] — O método `set` adiciona cabeçalhos à requisição e é o caminho para enviar token de portador, chave de API ou cabeçalhos condicionais específicos do caso.
876. [[supertest-timeouts]] — O cliente herdado do Superagent permite configurar tempo limite por resposta ou por prazo total, evitando que uma suíte fique pendurada indefinidamente.
877. [[supertest-binary-buffer-parsing]] — Respostas que não são JSON chegam ao teste como fluxo ou buffer, e a verificação precisa olhar bytes e cabeçalhos em vez de assumir corpo estruturado.
878. [[supertest-server-lifecycle]] — Ao receber a aplicação, o Supertest inicia um servidor em porta efêmera para a requisição e o encerra ao final, dispensando gerenciamento manual de porta na maioria dos casos.
879. [[supertest-against-express-router]] — O Supertest aceita a aplicação completa, um roteador ou uma função de tratamento, e a escolha define quais camadas — parsing, autenticação, middleware — participam do teste.

### Minitest — asserções, spec, mocks, ciclo de vida e paralelização

880. [[minitest-test-class-method-naming]] — Casos escritos em classes que herdam de `Minitest::Test` são descobertos pelos métodos cujo nome começa com `test_`, sem registro manual de suíte.
881. [[minitest-core-assertions]] — O módulo de asserções cobre igualdade, predicados, tipos, inclusão e referência, cada uma produzindo mensagem de falha específica para o tipo de comparação.
882. [[minitest-assert-raises]] — `assert_raises` falha se o bloco não levantar uma das exceções esperadas e devolve a exceção capturada para verificação de mensagem e atributos.
883. [[minitest-setup-teardown]] — Os métodos `setup` e `teardown` executam antes e depois de cada teste da classe, mantendo o estado de preparação isolado entre casos individuais.
884. [[minitest-spec-dsl]] — `Minitest::Spec` oferece `describe` e `it` com hooks `before`, `after` e `around`, além de matchers de expectativa para testes escritos em estilo de especificação.
885. [[minitest-mock-and-stub]] — `Minitest::Mock` registra expectativas e verifica chamadas ao final do teste, enquanto o método `stub` substitui um objeto por um retorno controlado durante o bloco.
886. [[minitest-parallelize-me]] — `parallelize_me!` executa os testes da classe em várias threads, reduzindo tempo total quando os casos são independentes entre si.
887. [[minitest-random-order-and-seed]] — O Minitest executa os testes em ordem aleatória por padrão e informa a semente usada, permitindo repetir a mesma sequência em caso de falha.
888. [[minitest-skip-and-flunk]] — `skip` interrompe o caso com motivo e o registra como pulado, enquanto `flunk` falha de propósito para marcar um caminho que nunca deveria ser alcançado.
889. [[minitest-reporters-and-run]] — O Minitest pode ser executado com `ruby -Ilib:test` em arquivos isolados, com `ruby -e` para carregar toda a suíte ou por integração com Rake e ferramentas de relatório.

### JaCoCo — agente, contadores, relatórios, verificação e instrumentação offline

890. [[jacoco-agent-on-the-fly]] — O agente do JaCoCo instrumenta classes em tempo de execução e grava os dados coletados em um arquivo binário de execução durante a JVM.
891. [[jacoco-counters-meaning]] — O JaCoCo contabiliza instruções, ramos, linhas, complexidade, métodos e classes, cada qual respondendo a uma pergunta distinta sobre a execução.
892. [[jacoco-branch-vs-line]] — A cobertura de ramos mede quantos desfechos de estruturas condicionais foram executados, incluindo os caminhos de `if` e de `switch`.
893. [[jacoco-report-formats]] — O goal de relatório gera HTML para leitura humana e pode produzir XML e CSV para consumo por outras ferramentas, todos derivados do mesmo arquivo de execução.
894. [[jacoco-check-rules-limits]] — O goal de verificação avalia regras compostas por elemento, contador, valor e limite, e pode interromper o build quando o mínimo configurado não é atingido.
895. [[jacoco-offline-instrumentation]] — Na instrumentação offline, as classes são transformadas antes da execução e os dados são gravados pela biblioteca de runtime, sem agente anexado à JVM.
896. [[jacoco-merge-exec-files]] — Quando a suíte roda em várias JVMs, cada processo gera dados próprios, e o goal de merge combina os arquivos em um único conjunto antes do relatório.
897. [[jacoco-excludes-filtering]] — Exclusões podem ser configuradas por classe, pacote, anotação ou expressão, removendo do relatório código que não é alvo de teste significativo.
898. [[jacoco-thresholds-policy]] — Cobertura descreve o que foi executado e não prova qualidade das asserções, portanto o limite deve expressar uma política de proteção contra regressão.
899. [[jacoco-build-integration]] — A integração típica encadeia preparação do agente, execução dos testes, geração de relatório e verificação, cada passo dependendo do anterior no ciclo do projeto.

### Maestro — fluxos YAML, comandos, tags, reuso e evidências

900. [[maestro-flow-yaml-structure]] — Um fluxo do Maestro é um arquivo YAML com identificador do aplicativo no cabeçalho, separador de documento e uma lista de comandos executados em ordem.
901. [[maestro-launch-and-state]] — `launchApp` inicia o aplicativo, `clearState` remove dados persistidos e `stopApp` encerra a execução, permitindo controlar o estado inicial de cada cenário.
902. [[maestro-tapon-selectors]] — O comando `tapOn` aceita texto visível, identificador de testabilidade e posição relativa, e a escolha do seletor define a estabilidade do passo.
903. [[maestro-assertions-and-waits]] — `assertVisible` e `assertNotVisible` verificam o estado da tela, e `extendedWaitUntil` aguarda uma condição com tempo limite antes de seguir.
904. [[maestro-runflow-subflows]] — O comando `runFlow` executa comandos de outro arquivo, aceita variáveis de ambiente e pode ser condicionado à visibilidade de um elemento.
905. [[maestro-input-and-keyboard]] — `inputText` digita em um campo focado, `eraseText` remove caracteres e `hideKeyboard` fecha o teclado virtual quando ele cobre a interface.
906. [[maestro-tags-and-filters]] — Tags declaradas no fluxo permitem selecionar subconjuntos na CLI com `--include-tags` e excluir grupos com `--exclude-tags`, usando lógica de união dentro de cada flag.
907. [[maestro-repeat-and-conditions]] — O comando `repeat` executa um bloco por número de vezes ou enquanto uma condição for verdadeira, permitindo cobrir listas e tentativas sem duplicar comandos.
908. [[maestro-screenshots-artifacts]] — O comando `takeScreenshot` e o diretório de saída da CLI registram imagens dos passos, e a execução pode produzir resultado em formato consumível pelo pipeline.
909. [[maestro-wait-animation-and-scroll]] — `waitForAnimationToEnd` aguarda a interface estabilizar e `scrollUntilVisible` rola a tela até o elemento aparecer, com limite de rolagem.

### Karate — feature files, asserções, configuração, paralelismo e mocks

910. [[karate-gherkin-builtin-steps]] — Arquivos de feature usam sintaxe Gherkin, mas os passos de HTTP, asserção e manipulação de dados já vêm implementados no framework.
911. [[karate-match-assertions]] — O comando `match` compara respostas com valores esperados e aceita marcadores como `#string`, `#number` e `#[]` para validar estrutura sem fixar conteúdo volátil.
912. [[karate-config-js]] — O arquivo `karate-config.js` é avaliado antes das features e devolve um objeto de configuração que pode variar conforme o ambiente selecionado.
913. [[karate-call-and-read]] — `call` executa outra feature como função em contexto isolado, `callonce` reaproveita o resultado e `read` carrega conteúdo de arquivo para os dados do cenário.
914. [[karate-parallel-runner]] — O runner do Karate executa features em paralelo por padrão quando configurado com um número de threads, mantendo cada cenário em contexto isolado.
915. [[karate-data-driven]] — Cenários podem ser repetidos com conjuntos de dados declarados em tabelas, `Examples` ou arquivos externos como CSV, mantendo a lógica única e os dados separados.
916. [[karate-tags-selection]] — Tags declaradas em features e cenários permitem selecionar subconjuntos por execução, incluindo ou excluindo grupos conforme a necessidade do pipeline.
917. [[karate-mock-server]] — O servidor mock do Karate descreve rotas, respostas e validações em feature files, cobrindo contratos antes de o serviço real existir.
918. [[karate-print-and-debug]] — O comando `print` exibe valores no relatório e a resposta completa pode ser inspecionada para diagnóstico quando a asserção falha.
919. [[karate-reports-artifacts]] — O runner gera relatório HTML com o detalhamento de cada feature, cenário e passo, além de artefatos consumíveis por ferramentas de integração contínua.

### Swift Testing — macros, suítes, traits, parametrização e migração

920. [[swift-testing-test-macro]] — A macro `@Test` identifica uma função de teste, dispensando herança de classe e o prefixo `test` no nome do método.
921. [[swift-testing-expect-and-require]] — `#expect` registra uma falha e continua a execução, enquanto `#require` interrompe o teste ao falhar e devolve o valor desembrulhado.
922. [[swift-testing-suites-and-lifecycle]] — Qualquer tipo que contenha funções de teste forma uma suíte, e a anotação `@Suite` é necessária apenas para nome, traits ou agrupamento explícito.
923. [[swift-testing-parameterized-tests]] — A macro `@Test(arguments:)` executa a mesma função para cada argumento, gerando um resultado pai com um filho por valor ou combinação.
924. [[swift-testing-traits]] — Traits são valores aplicados a testes e suítes para desabilitar, condicionar, limitar tempo, marcar tags e registrar referências de defeito.
925. [[swift-testing-tags]] — Tags declaradas em extensões do tipo `Tag` permitem rotular testes e suítes para organização e filtragem em planos de teste.
926. [[swift-testing-serialized]] — Testes rodam em paralelo por padrão e a trait `.serialized` restringe a execução de uma suíte à ordem sequencial.
927. [[swift-testing-async-tests]] — Funções de teste podem ser `async` e aguardar operações diretamente, sem expectativas de inversão de controle nem callbacks de conclusão.
928. [[swift-testing-migration-from-xctest]] — A migração converte classes `XCTestCase` em suítes, métodos com prefixo em funções `@Test` e asserções específicas nas macros de expectativa.
929. [[swift-testing-swift-test-cli]] — O comando `swift test` do SwiftPM descobre e executa os testes do pacote, incluindo os escritos com Swift Testing em toolchains compatíveis.

### MSTest — estrutura, dados, ciclo de vida, paralelização e configuração

930. [[mstest-testclass-and-testmethod]] — Métodos de teste são marcados com `[TestMethod]` dentro de classes anotadas com `[TestClass]`, e precisam ser públicos, de instância e sem parâmetros fora de casos com dados.
931. [[mstest-datarow-inline]] — O atributo `[DataRow]` declara valores constantes para os parâmetros do teste, e cada linha gera uma execução independente identificada pelos dados.
932. [[mstest-dynamicdata-provider]] — O atributo `[DynamicData]` referencia uma propriedade ou método que devolve uma coleção de linhas, permitindo dados calculados ou objetos tipados.
933. [[mstest-lifecycle-order]] — A inicialização e a limpeza acontecem em níveis de assembly, classe e teste, e o nível de teste se repete para cada linha de dados parametrizados.
934. [[mstest-testcontext]] — O executor injeta um objeto `TestContext` no teste, oferecendo informações de execução, resultado da linha de dados e saída de diagnóstico associada ao caso.
935. [[mstest-assertions-and-exceptions]] — O tipo `Assert` reúne comparações de igualdade, verificações de coleção e asserções de exceção que falham com mensagem específica.
936. [[mstest-parallelization]] — A paralelização pode ser declarada por atributo de assembly com escopo e número de trabalhadores, ou configurada globalmente em runsettings ou testconfig.
937. [[mstest-timeout-and-retry]] — Atributos de tempo limite e de repetição permitem interromper operação longa e repetir um caso falho antes de considerá-lo reprovado.
938. [[mstest-categories-and-filtering]] — Atributos de categoria e propriedade rotulam testes para filtragem no executor, permitindo selecionar subconjuntos por tipo ou risco.
939. [[mstest-runsettings-vs-testconfig]] — Executores baseados na plataforma de testes leem `testconfig.json`, enquanto o caminho clássico usa `.runsettings` para paralelização, timeouts e demais ajustes.

### cargo-nextest — isolamento, perfis, retries, partições e relatórios

940. [[nextest-process-per-test]] — O nextest agenda cada teste como um processo separado, em vez de compartilhar o binário de teste entre vários casos como faz o executor padrão.
941. [[nextest-profiles]] — Configurações ficam em arquivo de perfil no workspace, com um perfil padrão e perfis nomeados que podem ser selecionados na linha de comando.
942. [[nextest-retries-and-flaky-result]] — Retries configuram quantas vezes um teste falho é repetido, e a política de resultado define se a execução final conta como falha ou como instável.
943. [[nextest-slow-timeout]] — O limite de lentidão avisa quando um teste excede o período configurado e pode encerrá-lo após um número de períodos.
944. [[nextest-filtersets]] — Expressões de filtro permitem selecionar casos por nome, pacote, tipo de teste e outras propriedades diretamente na linha de comando.
945. [[nextest-partitioning]] — O particionamento divide os testes em fatias ou por hash de identificador, permitindo distribuir a mesma suíte entre executores paralelos.
946. [[nextest-junit-report]] — O nextest pode gravar relatório JUnit XML por perfil, com opções para incluir ou omitir saída de testes aprovados e para classificar resultados instáveis.
947. [[nextest-archives]] — O comando de arquivamento empacota os binários de teste compilados para que outra etapa ou máquina execute o mesmo build sem recompilar.
948. [[nextest-doctests-boundary]] — O nextest executa binários de teste compilados e não cobre exemplos de documentação, que continuam precisando do comando clássico do Cargo.
949. [[nextest-listing-and-ignored]] — O comando de listagem mostra o conjunto descoberto sem executar, e a opção de execução de ignorados permite rodar casos marcados como pendentes.

## Tranche 16 — desempenho, cobertura, acessibilidade e contratos

### Detox — testes end-to-end de React Native com sincronização de dispositivo

950. [[detox-synchronization-gray-box]] — O Detox observa rede, temporizadores e animações do aplicativo e espera a estabilização antes de executar cada ação ou asserção.
951. [[detox-testid-selectors]] — Matchers baseados em identificador procuram o valor de testabilidade definido no componente, enquanto texto e rótulo dependem de conteúdo visível.
952. [[detox-launchapp-options]] — A chamada de lançamento aceita opções como instância nova, permissões de sistema, argumentos e abertura por link, definindo o estado inicial do cenário.
953. [[detox-reload-react-native]] — A recarga do pacote JavaScript restaura o estado da aplicação sem reconstruir o binário nem reiniciar o processo nativo, reduzindo o tempo entre casos.
954. [[detox-waitfor-explicit]] — A espera explícita por um elemento aceita limite de tempo e pode rolar uma lista até o alvo aparecer, cobrindo eventos que a sincronização padrão não acompanha.
955. [[detox-assertions-visibility-existence]] — As asserções de visibilidade verificam o que está apresentado na tela, enquanto as de existência apenas confirmam que o elemento está montado na hierarquia.
956. [[detox-disable-synchronization-scope]] — A sincronização pode ser desativada e reativada durante o teste, delimitando um trecho em que a ferramenta não aguarda operações pendentes.
957. [[detox-device-actions]] — Ações de dispositivo cobrem operações fora da árvore de interface, como enviar o aplicativo ao segundo plano, retomá-lo e capturar a tela em um ponto nomeado.
958. [[detox-artifacts-failure]] — A execução pode capturar telas e gravar vídeos nos casos que falham, produzindo evidência sem exigir reprodução local do problema.
959. [[detox-configuration-file]] — O arquivo de configuração declara aplicativos, dispositivos e configurações nomeadas usadas pelos comandos de build e de teste.
960. [[detox-ci-stability]] — Ambientes de integração contínua sofrem com animações habilitadas, emuladores lentos e recursos limitados, o que altera o tempo das transições.

### Artillery — fases de carga, cenários HTTP e limites de desempenho

961. [[artillery-load-phases]] — Cada fase informa duração e taxa de chegada de usuários virtuais, e a opção de progressão transforma a taxa inicial em taxa final ao longo do período.
962. [[artillery-scenario-flow]] — O bloco de cenários descreve a sequência de passos que cada usuário virtual executa, incluindo requisições, pausas e agrupamentos.
963. [[artillery-capture-and-reuse]] — Valores extraídos da resposta podem ser guardados em variáveis nomeadas e reutilizados nos passos seguintes do mesmo cenário.
964. [[artillery-thresholds]] — A extensão de verificação compara métricas da execução com limites declarados e encerra com código de erro quando algum deles é ultrapassado.
965. [[artillery-metrics-interpretation]] — Durante a execução a ferramenta publica resumo periódico, e ao final apresenta contagens de cenários, requisições, taxas e distribuição de latência.
966. [[artillery-browser-engine]] — Além de requisições HTTP, a ferramenta aceita mecanismo que controla navegador real, permitindo medir carregamento completo de páginas sob carga.
967. [[artillery-expect-plugin]] — A extensão de asserções permite declarar condições sobre cada resposta, como código de status e campo do corpo, falhando o passo quando o contrato não é atendido.
968. [[artillery-quick-and-run]] — O comando de execução rápida parte de um alvo e gera um cenário mínimo para verificação imediata, enquanto a execução por arquivo usa a definição completa.
969. [[artillery-scenario-weights]] — Cenários podem receber pesos relativos, fazendo com que a carga gerada combine jornadas distintas na proporção declarada.
970. [[artillery-rate-vs-concurrency]] — A ferramenta modela taxa de chegada de usuários virtuais ao longo do tempo, e não uma quantidade fixa de requisições por segundo.
971. [[artillery-ci-integration]] — A execução pode gravar o resumo em arquivo e devolver código de erro pelos limites, permitindo que a verificação de desempenho participe do fluxo automático.

### Vegeta — ataques HTTP de taxa constante, relatórios e análise

972. [[vegeta-attack-basics]] — O subcomando de ataque recebe alvos, uma taxa em requisições por segundo e uma duração, emitindo um fluxo binário com os resultados.
973. [[vegeta-targets-file]] — O arquivo de alvos contém método e URL por linha, aceitando cabeçalhos adicionais no bloco seguinte e referência a arquivo de corpo para requisições que enviam dados.
974. [[vegeta-report-metrics]] — O subcomando de relatório resume o fluxo de resultados com latências por percentil, taxa efetiva, volume de dados e proporção de sucesso.
975. [[vegeta-plot-timeline]] — O subcomando de gráfico gera uma página com série temporal de latências, permitindo correlacionar picos com eventos ocorridos durante o ataque.
976. [[vegeta-encode-and-dump]] — Os subcomandos de codificação e descarga convertem o fluxo binário em formatos legíveis, como JSON e CSV, permitindo consumo por ferramentas de análise.
977. [[vegeta-rate-workers-connections]] — A taxa define quantas requisições iniciar por segundo, os trabalhadores definem o paralelismo inicial e as conexões limitam conexões ociosas por host.
978. [[vegeta-timeouts-and-transport]] — O ataque aceita tempo limite por requisição, conexões persistentes, negociação de versão do protocolo e opções de certificado para ambientes de teste.
979. [[vegeta-thresholds-in-ci]] — O relatório pode ser emitido em formato estruturado, o que permite extrair percentuais e proporções e reprovar a execução quando os valores desviam do esperado.
980. [[vegeta-library-usage]] — A ferramenta expõe biblioteca em Go que permite definir alvos dinâmicos, alimentar dados variáveis e consumir resultados no mesmo processo.
981. [[vegeta-load-model-limits]] — O ataque mantém taxa fixa de início de requisições, comportamento que difere de sistemas reais com usuários que esperam respostas antes de agir.

### JMH — microbenchmarks de JVM com aquecimento, estados e modos de medição

982. [[jmh-benchmark-annotation]] — O método anotado como benchmark é envolvido em código gerado que executa e mede repetidamente a mesma operação.
983. [[jmh-blackhole-consumption]] — A estrutura oferece objeto de consumo que registra o valor produzido, impedindo que o compilador remova o cálculo por falta de uso aparente.
984. [[jmh-modes]] — Os modos disponíveis medem vazão por unidade de tempo, tempo médio por operação, amostragem de distribuição e execução única.
985. [[jmh-warmup-and-measurement]] — As anotações definem quantas iterações preparam a máquina virtual e quantas produzem os números que entram no relatório.
986. [[jmh-forking]] — O parâmetro de fork define quantos processos independentes executam o benchmark, cada um com sua própria máquina virtual.
987. [[jmh-state-scope]] — O escopo do objeto de estado define se os dados são compartilhados entre threads, exclusivos de cada thread ou limitados a um grupo.
988. [[jmh-setup-and-teardown]] — A preparação e a limpeza podem ocorrer uma vez por execução, por iteração ou por invocação, conforme o nível escolhido.
989. [[jmh-parameters]] — Campos anotados como parâmetros recebem cada valor declarado, e o benchmark é expandido em uma execução por combinação de valores.
990. [[jmh-profiling-aids]] — A execução aceita perfis embutidos, como contabilização de coleta de lixo, e permite escolher perfiladores externos por linha de comando.
991. [[jmh-execution-and-pitfalls]] — A ferramenta pode ser executada por linha de comando a partir de artefato construído ou por chamada programática em método principal.

### coverage.py — execução instrumentada, ramos, configuração e relatórios

992. [[coveragepy-run-basics]] — O comando de execução instrumenta o interpretador, roda o módulo ou script indicado e grava os dados coletados em arquivo.
993. [[coveragepy-branch-coverage]] — Com cobertura de ramos ativa, a medição registra quais desfechos de decisões foram executados, inclusive caminhos parciais de expressões lógicas.
994. [[coveragepy-config-files]] — As opções podem ser declaradas em arquivo próprio, no arquivo de configuração do projeto ou no empacotamento, com precedência definida.
995. [[coveragepy-omit-and-exclude]] — Padrões de omissão removem arquivos inteiros da medição, e comentários ou expressões de exclusão removem linhas específicas do cálculo.
996. [[coveragepy-parallel-and-combine]] — O modo paralelo faz cada processo gravar arquivo próprio, e os arquivos podem ser combinados antes da geração dos relatórios.
997. [[coveragepy-fail-under]] — A opção de limite mínimo faz o comando terminar com código de erro quando o total fica abaixo do valor definido, tanto na configuração quanto na linha de comando.
998. [[coveragepy-report-formats]] — A ferramenta gera resumo em terminal, página navegável, formato estruturado e formato de intercâmbio, todos derivados dos mesmos dados.
999. [[coveragepy-contexts]] — Cada execução pode receber um rótulo e os relatórios podem filtrar por expressão sobre esses contextos, distinguindo o que cada tipo de teste cobre.
1000. [[coveragepy-subprocesses]] — Processos filhos iniciados durante a execução só são medidos quando a instrumentação é propagada por configuração de ambiente ou por opção de simultaneidade.
1001. [[coveragepy-limits-and-quality]] — Percentual de linhas e ramos descreve o que foi executado, sem atestar que as asserções verificam o comportamento correto.

### nyc e Istanbul — instrumentação JavaScript, limites e consolidação

1002. [[nyc-wrap-command]] — A ferramenta envolve o comando informado, instrumentando os módulos carregados durante a execução e gravando dados brutos em diretório temporário.
1003. [[nyc-all-and-filters]] — A opção de instrumentar tudo faz a medição abranger arquivos que a suíte não carregou, e os filtros de inclusão e exclusão delimitam esse conjunto.
1004. [[nyc-negated-excludes]] — Na lista de exclusão, um padrão iniciado por exclamação restaura caminhos que seriam removidos pela regra anterior ou padrão.
1005. [[nyc-reporters]] — A lista de geradores define os formatos produzidos, e o diretório de relatórios concentra os artefatos publicados.
1006. [[nyc-check-coverage-thresholds]] — A verificação de cobertura compara cada métrica com o limite declarado e encerra com erro quando algum valor fica abaixo do mínimo.
1007. [[nyc-temp-dir-and-merge]] — Os dados brutos ficam no diretório temporário, e a ferramenta permite mesclar arquivos de execuções distintas antes de gerar o relatório consolidado.
1008. [[nyc-typescript-and-source-maps]] — Quando o teste executa código traduzido, os relatórios precisam mapear posições de volta ao original para apontar linhas úteis.
1009. [[nyc-project-root-and-monorepo]] — A raiz do projeto orienta a busca de fontes, a formação de padrões e a localização dos diretórios de artefato.
1010. [[nyc-ci-multi-job]] — Cada trabalho do pipeline publica seu diretório de dados brutos como artefato, e uma etapa final baixa todos, mescla e publica o resultado consolidado.
1011. [[nyc-excludes-and-generated-code]] — Artefatos produzidos por geradores de contrato e de esquema entram na medição quando os padrões não os alcançam.
1012. [[nyc-interpreting-numbers]] — Statements, branches, functions e lines medem dimensões distintas, e um arquivo pode estar integralmente coberto em uma delas e descoberto em outra.

### Lighthouse CI — coleta, asserções, orçamentos e publicação de métricas web

1013. [[lighthouseci-autorun-steps]] — O comando automático encadeia coleta das auditorias, verificação das asserções e publicação dos resultados em uma única execução.
1014. [[lighthouseci-collect-targets]] — A coleta recebe uma lista de endereços, um diretório estático ou um comando que sobe o servidor, com padrão e prazo para considerar o serviço pronto.
1015. [[lighthouseci-number-of-runs]] — A configuração permite repetir a auditoria várias vezes por página e consolidar o resultado, geralmente pelo valor mediano.
1016. [[lighthouseci-assertions-presets]] — A verificação aceita um conjunto pré-definido de regras e permite desligar ou ajustar itens específicos, com nível de erro ou aviso.
1017. [[lighthouseci-numeric-assertions]] — Asserções podem fixar pontuação mínima ou valor máximo de métrica, com escolha do método de agregação entre as repetições.
1018. [[lighthouseci-performance-budgets]] — Um arquivo de orçamento declara limites de tamanho ou quantidade por tipo de recurso, e a auditoria correspondente pode ser verificada na esteira.
1019. [[lighthouseci-upload-targets]] — A publicação pode enviar ao armazenamento temporário público, gravar em diretório local ou integrar servidor próprio com histórico.
1020. [[lighthouseci-config-file]] — A configuração pode ficar em arquivo JavaScript, JSON ou YAML, com seções para coleta, verificação, publicação, servidor e assistente.
1021. [[lighthouseci-artifacts-and-reports]] — A coleta grava relatórios e um manifesto no diretório de resultados, e há comando para abrir as páginas geradas localmente.
1022. [[lighthouseci-limits-in-ci]] — Métricas de laboratório sofrem influência do executor, e diferenças pequenas entre revisões podem não corresponder a mudança de código.

### Pa11y — varredura de acessibilidade, padrões, ações e limites de automação

1023. [[pa11y-cli-basics]] — O comando recebe um endereço, abre a página em navegador sem interface e aplica verificações do motor escolhido, reportando os problemas encontrados.
1024. [[pa11y-standards-and-levels]] — O nível de conformidade pode ser declarado entre os três níveis de acessibilidade e é usado apenas pelo motor baseado em regras estáticas.
1025. [[pa11y-runners]] — A ferramenta aceita dois motores distintos de análise, e cada um mantém conjunto próprio de regras e forma de reportar resultados.
1026. [[pa11y-actions]] — Uma lista de ações executada antes da análise permite preencher campos, acionar botões e esperar mudanças de endereço, alcançando estados que exigem interação.
1027. [[pa11y-reporters-and-exit]] — A ferramenta oferece relatórios em texto, formato estruturado e formato de valores separados, e o código de saída indica se o limite de problemas foi excedido.
1028. [[pa11y-threshold-policy]] — Um limite numérico permite que a execução passe com quantidade pequena de problemas, controlado por parâmetro ou configuração.
1029. [[pa11y-ignore-and-scope]] — Regras específicas podem ser ignoradas, e a análise pode ser limitada a um elemento raiz ou excluir trechos selecionados da página.
1030. [[pa11y-config-file]] — As opções podem ser reunidas em arquivo de configuração, o que mantém a linha de comando curta e documenta o comportamento esperado.
1031. [[pa11y-ci-multiple-urls]] — A ferramenta complementar lê uma lista de endereços em arquivo de configuração ou os descobre por mapa do site e produz resumo conjunto da varredura.
1032. [[pa11y-ci-environment]] — A configuração pode declarar argumentos de lançamento do navegador, tempo limite e espera inicial, além de ajustes necessários em contêineres.
1033. [[pa11y-automation-limits]] — A varredura detecta parte dos problemas de acessibilidade, mas não avalia qualidade da experiência com tecnologia assistiva real.

### Prism — simulação e validação de contratos HTTP a partir de especificação

1034. [[prism-mock-mode]] — O comando de simulação lê um documento de contrato e expõe rotas que respondem conforme os exemplos ou os esquemas descritos nele.
1035. [[prism-static-vs-dynamic]] — O modo predefinido responde com os exemplos declarados no contrato, enquanto o modo dinâmico gera valores a partir dos esquemas.
1036. [[prism-prefer-header]] — O cabeçalho de preferência permite escolher código de resposta, exemplo específico e modo de geração para uma requisição simulada.
1037. [[prism-validation-errors]] — Na função de proxy, requisições que não respeitam o contrato são reportadas e podem ser rejeitadas com resposta de erro estruturada.
1038. [[prism-proxy-mode]] — O modo de intermediação encaminha requisições ao serviço real e pode comparar o tráfego com a especificação, mantendo o trânsito inalterado quando não há modo estrito.
1039. [[prism-generated-errors]] — Quando a requisição não corresponde ao contrato, a ferramenta responde com documento de problema estruturado e cabeçalho descrevendo a violação.
1040. [[prism-spec-quality]] — Rotas, parâmetros e respostas simuladas derivam diretamente do documento, e imprecisões aparecem como comportamento inesperado do servidor.
1041. [[prism-cli-workflow]] — A ferramenta de linha de comando oferece execução do servidor de simulação e do intermediário, com opções de porta, modo estrito e hospedagem do documento a partir de endereço remoto.
1042. [[prism-client-programmatic]] — A biblioteca permite criar instância de simulação a partir de operações específicas do contrato, com opções de geração dinâmica, validação e erro.
1043. [[prism-contract-first-workflow]] — A simulação só é útil quando o contrato é a fonte acordada entre quem consome e quem fornece, mantido antes da implementação.
1044. [[prism-limits]] — A ferramenta reproduz respostas previstas no contrato, sem manter estado entre chamadas nem aplicar regras de negócio.

### Hurl — arquivos de requisição, capturas, asserções e execução em lote

1045. [[hurl-file-structure]] — O arquivo descreve uma entrada com a requisição e, opcionalmente, a resposta esperada logo abaixo, incluindo código de status e cabeçalhos.
1046. [[hurl-implicit-assertions]] — Cabeçalhos declarados na resposta esperada são verificados automaticamente, sem necessidade de bloco explícito de asserções.
1047. [[hurl-captures]] — O bloco de capturas extrai valores da resposta por expressão e os disponibiliza como variáveis para as entradas seguintes do arquivo.
1048. [[hurl-assertions]] — O bloco de asserções aceita consultas ao corpo estruturado, contagens, comparações textuais e verificação de existência de cabeçalhos.
1049. [[hurl-status-and-error-handling]] — A execução considera falha quando a resposta diverge do esperado, e o código de saída indica se houve erro de asserção, de execução ou de configuração.
1050. [[hurl-options-block]] — O bloco de opções permite declarar por entrada ajustes como repetição com intervalo, atraso entre requisições e política de continuidade após erro.
1051. [[hurl-cli-test-mode]] — O modo de teste recebe arquivos ou diretórios, executa em paralelo com número controlado de tarefas e apresenta resumo por arquivo.
1052. [[hurl-session-scope]] — As entradas de um mesmo arquivo compartilham sessão, o que mantém cookies e variáveis entre requisições, enquanto arquivos distintos não compartilham.
1053. [[hurl-variables-and-reports]] — Variáveis podem ser definidas por linha de comando ou arquivo, e a execução gera relatórios em formatos de página e de resultado de testes.
1054. [[hurl-ci-integration]] — O código de saída e os relatórios permitem integrar a verificação de contrato a um pipeline, com recapitulação legível e resultado consumível por máquina.
1055. [[hurl-contract-verification-limits]] — Os arquivos verificam forma e valores das respostas que o serviço realmente devolve, sem validar a especificação nem substituir testes de comportamento.

## Estado editorial

O gate automatizado foi aprovado por 1055/1055 notas e as 1055 contam como válidas pelo protocolo atualizado: nove têm aprovação humana histórica e 1046 têm revisão factual por IA registrada separadamente. O lote de 2.000 continua `in_progress` (1055 notas substantivas; 945 ainda não produzidas). Consulte o [manifesto](../../exports/batches/software-testes-2000-0001.md), a [auditoria de qualidade](../../exports/reports/note-quality-software-testes-2000-0001.md) e a [reconciliação mais recente do manifesto/fila](../../exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-16.md). Os relatórios factuais por IA são [tranches 2–3](../../exports/reports/ai-review-software-testes-2000-0001.md), [4](../../exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](../../exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](../../exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](../../exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](../../exports/reports/ai-review-software-testes-2000-0001-tranche-08.md), [9](../../exports/reports/ai-review-software-testes-2000-0001-tranche-09.md), [10](../../exports/reports/ai-review-software-testes-2000-0001-tranche-10.md), [11](../../exports/reports/ai-review-software-testes-2000-0001-tranche-11.md) e [12](../../exports/reports/ai-review-software-testes-2000-0001-tranche-12.md), [13](../../exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](../../exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](../../exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e [16](../../exports/reports/ai-review-software-testes-2000-0001-tranche-16.md). Consulte também o [registro de revisão humana e IA](../../exports/reports/human-review-queue.md).
